from hashlib import md5
from os import listdir
from os.path import join


def get_directory_tree(dirpath):
    tree = {}

    for f in listdir(dirpath):
        subdirs = listdir(join(dirpath, f))
        tree[f] = {}

        if subdirs:
            for s in subdirs:
                if "Chapter" not in s:
                    tree[f][s] = {}

                    for d in listdir(join(dirpath, f, s)):
                        tree[f][s][d] = []

                        for p in listdir(join(dirpath, f, s, d)):
                            tree[f][s][d].append(p)
                else:
                    tree[f][s] = []
                    for p in listdir(join(dirpath, f, s)):
                        tree[f][s].append(p)
    return tree


def tree2db(tree):
    from toshokan import app, db
    from toshokan.series.models import Series, Volume, Doujinshi, Chapter, Page

    series = Series.query.filter(Series.name == tree[0]).first()

    if not series:
        series = Series(tree[0])
        db.session.add(series)
        db.session.commit()

    for subunit in tree[1].items():
        if "Volume" in subunit[0]:
            vol_num = subunit[0].split(" ")

            try:
                volume = Volume.query.filter(Volume.number == int(vol_num[1]), Volume.series_id == series.id).first()

                if not volume:
                    volume = Volume(int(vol_num[1]))
                    series.volumes.append(volume)
                    db.session.commit()

                for chap in subunit[1].items():
                    chap_num = chap[0].split(" ")

                    try:
                        chapter = Chapter.query.filter(Chapter.number == int(chap_num[1]), Chapter.volume_id == volume.id).first()

                        if not chapter:
                            chapter = Chapter(int(chap_num[1]))
                            volume.chapters.append(chapter)
                            db.session.commit()

                        for p in chap[1]:
                            _p = p.split(".")

                            if _p[1] in ["jpg", "jpeg", "png"]:
                                loc = join(str(app.config['LIBRARY']), series.name, "Volume %s" % volume.number, "Chapter %s" % chapter.number, p)
                                file = open(loc, 'rb').read()
                                _md5 = md5(file).hexdigest()

                                try:
                                    page = Page.query.filter(Page.number == int(_p[0]), Page.chapter_id == chapter.id).first()

                                    if not page:
                                        page = Page(int(_p[0]), p, _md5)
                                        chapter.pages.append(page)
                                        db.session.commit()

                                    if page.md5 != _md5:
                                        page.md5 = _md5
                                        db.session.commit()
                                except ValueError:
                                    continue
                            else:
                                continue
                    except ValueError:
                        continue
            except ValueError:
                continue

        elif "Doujinshi" in subunit[0]:
            continue
        else:
            continue


def scan_directory(directory):
    return listdir(directory)
