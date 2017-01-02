from os.path import join

from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_resize import Resize
from flask_sqlalchemy import SQLAlchemy

from .utils import get_directory_tree, scan_directory, tree2db


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle("scss/main.scss", filters='pyscss', output="css/main.css")
assets.register('scss_all', scss)

resize = Resize(app)


@app.route('/')
def home():
    return render_template("main.html", title="Home", page="home")


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
