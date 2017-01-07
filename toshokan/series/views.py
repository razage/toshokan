from flask import abort, Blueprint, render_template
from flask_restful import Api, Resource

from .models import Chapter, Series, Volume
from .schemas import SeriesSchema, VolumeSchema

mod = Blueprint("series", __name__, url_prefix="/series")
api = Api(mod)


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
                           cdir="%s/Volume %s/Chapter %s/" % (c.volume.series.name, c.volume.number, c.number))


class SeriesList(Resource):
    schema = SeriesSchema()

    def get(self):
        return self.schema.jsonify(Series.query.order_by(Series.name).all(), many=True)


class SeriesResource(Resource):
    schema = SeriesSchema()

    def get(self, sid):
        s = Series.query.get_or_404(sid)
        return self.schema.jsonify(s)


class VolumeResource(Resource):
    schema = VolumeSchema()

    def get(self, sid, vid):
        v = Volume.query.filter(Volume.series_id == sid, Volume.id == vid).first()
        return self.schema.jsonify(v)

api.add_resource(SeriesList, "/")
api.add_resource(SeriesResource, "/<int:sid>")
api.add_resource(VolumeResource, "/<int:sid>/<int:vid>")
