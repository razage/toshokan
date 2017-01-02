from os.path import join

from flask import abort, Blueprint, render_template

from toshokan import app
from .models import Chapter, Series, Volume

mod = Blueprint("series", __name__, url_prefix="/series")


@mod.route("/<int:sid>")
def series_view(sid):
    s = Series.query.get_or_404(sid)
    return render_template("series/series_view.html", title=s.name, page="toshokan", series=s)


@mod.route("/<int:sid>/<int:vid>/chapters/")
def series_chapter_view(sid, vid):
    v = Volume.query.filter(Volume.series_id == sid, Volume.id == vid).first()

    if not v:
        abort(404)

    return render_template("series/chapters_view.html", title="%s Volume %s Chapters" % (v.series.name, v.number),
                           page="toshokan", series=v.series, volume=v)


@mod.route("/<int:sid>/<int:vid>/chapters/<int:cid>")
def series_chapter_page_view(sid, vid, cid):
    c = Chapter.query.filter(Chapter.id == cid).first()

    if not c:
        abort(404)

    return render_template("series/pages_view.html",
                           title="%s Volume %s Chapter %s" % (c.volume.series.name, c.volume.number, c.number),
                           page="toshokan", series=c.volume.series, chapter=c,
                           cdir="manga/%s/Volume %s/Chapter %s/" % (c.volume.series.name, c.volume.number, c.number))
