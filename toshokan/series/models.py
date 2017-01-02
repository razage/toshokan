from toshokan import db
from toshokan.models import BaseModel


class Page(BaseModel):
    __tablename__ = "pages"
    __table_args__ = tuple(db.UniqueConstraint("chapter_id", "number", name="_chapter_page_uc"))
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id"))
    number = db.Column(db.Integer)
    filename = db.Column(db.String(64))
    md5 = db.Column(db.String(64))

    chapter = db.relationship("Chapter", backref="pages", foreign_keys=chapter_id)

    def __init__(self, number, filename, md5):
        self.number = number
        self.filename = filename
        self.md5 = md5


class Chapter(BaseModel):
    __tablename__ = "chapters"
    __table_args__ = tuple(db.UniqueConstraint("volume_id", "number", name='_volume_chapter_uc'))
    volume_id = db.Column(db.Integer, db.ForeignKey("volumes.id"))
    doujin_id = db.Column(db.Integer, db.ForeignKey("doujinshi.id"))
    name = db.Column(db.String(32), nullable=True)
    number = db.Column(db.Integer)

    volume = db.relationship("Volume", backref="chapters", foreign_keys=volume_id)
    doujin = db.relationship("Doujinshi", backref="chapters", foreign_keys=doujin_id)

    def __init__(self, number):
        self.number = number

    @property
    def page_count(self):
        return len(self.pages)


class Volume(BaseModel):
    __tablename__ = "volumes"
    __table_args__ = tuple(db.UniqueConstraint("series_id", "number", name='_series_volume_uc'))
    series_id = db.Column(db.Integer, db.ForeignKey("series.id"))
    name = db.Column(db.String(32), nullable=True)
    number = db.Column(db.Integer)

    series = db.relationship("Series", backref="volumes", foreign_keys=series_id)

    def __init__(self, number):
        self.number = number

    @property
    def page_count(self):
        _count = 0

        for c in self.chapters:
            _count += c.page_count

        return _count


class Doujinshi(BaseModel):
    __tablename__ = "doujinshi"
    series_id = db.Column(db.Integer, db.ForeignKey("series.id"))
    name = db.Column(db.String(32))
    artist = db.Column(db.String(32), nullable=True)
    group = db.Column(db.String(32), nullable=True)

    series = db.relationship("Series", backref="doujins", foreign_keys=series_id)

    def __init__(self, name, artist=None, group=None):
        self.name = name
        self.artist = artist
        self.group = group


class Series(BaseModel):
    __tablename__ = "series"
    name = db.Column(db.String(32), unique=True)
    author = db.Column(db.String(32), nullable=True)
    age_rating = db.Column(db.String(5), nullable=True)

    def __init__(self, name, author=None, age_rating=None):
        self.name = name
        self.author = author
        self.age_rating = age_rating
