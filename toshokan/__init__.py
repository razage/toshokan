from os.path import join

from flask import Flask, render_template, send_from_directory
from flask_assets import Environment, Bundle
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from .utils import get_directory_tree, scan_directory, tree2db

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle("scss/main.scss", filters='pyscss', output="css/compiled.css")
css = Bundle("bower_components/jquery-ui/themes/base/jquery-ui.css", scss, filters="cssmin", output="css/main.css")

assets.register('css_all', css)


@app.route('/')
def home():
    return render_template("main.html", title="Home", page="home")


@app.route('/manga/<path:filename>')
def manga(filename):
    return send_from_directory(str(app.config['LIBRARY']), filename)


@app.route('/update')
def update_library():
    from toshokan.series.models import Series, Volume, Doujinshi, Chapter, Page

    base_dir = str(app.config['LIBRARY'])
    library = scan_directory(str(app.config['LIBRARY']))
    library_structure = {}

    for l in library:
        library_structure[l] = get_directory_tree(join(base_dir, l))

    for series in library_structure.items():
        tree2db(series)

    return "Nothing"


from toshokan.library.views import mod as library_mod
from toshokan.series.views import mod as series_mod

app.register_blueprint(library_mod)
app.register_blueprint(series_mod)
