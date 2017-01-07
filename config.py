from json import dump, load
from os.path import abspath, dirname, join
from pathlib import Path
from random import SystemRandom

BASEDIR = abspath(dirname(__file__))
SETTINGS = Path(join(BASEDIR, "settings.json"))

if SETTINGS.is_file():
    conf = load(open(str(SETTINGS)))
else:
    skey = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    conf = {"db_type": "sqlite", "secret_key": skey, "manga_dir": "path to your base manga directory"}
    dump(conf, open(str(SETTINGS), 'w'))

if conf['db_type'] == "sqlite":
    DB = Path(join(BASEDIR, "database.db"))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(DB)
else:
    raise KeyError("db_type not defined in the config!")

SECRET_KEY = conf['secret_key']
WTF_CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

LIBRARY = Path(conf['manga_dir'])
