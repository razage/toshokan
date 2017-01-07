from toshokan import ma
from .models import Chapter, Doujinshi, Page, Series, Volume


class PageSchema(ma.ModelSchema):
    class Meta:
        table = Page
        fields = ("id", "number", "filename", "md5")


class ChapterSchema(ma.ModelSchema):
    class Meta:
        table = Chapter
        fields = ("id", "name", "number", "pages")

    pages = ma.Nested(PageSchema, many=True)


class DoujinshiSchema(ma.ModelSchema):
    class Meta:
        table = Doujinshi
        fields = ("id", "name", "artist", "group", "chapters")

    chapters = ma.Nested(ChapterSchema, many=True)


class VolumeSchema(ma.ModelSchema):
    class Meta:
        table = Volume
        fields = ("id", "name", "number", "chapters")

    chapters = ma.Nested(ChapterSchema, many=True)


class SeriesSchema(ma.ModelSchema):
    class Meta:
        table = Series
        fields = ("id", "name", "author", "age_rating", "volumes", "doujins")

    volumes = ma.Nested(VolumeSchema, many=True)
    doujins = ma.Nested(DoujinshiSchema, many=True)
