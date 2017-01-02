from flask import Blueprint, render_template

from toshokan.series.models import Series

mod = Blueprint("library", __name__, url_prefix="/toshokan")


@mod.route("/")
def library_home():
    series = Series.query.order_by(Series.name).all()
    return render_template("library/library_view.html", title="Manga Toshokan", page="toshokan", series=series)
