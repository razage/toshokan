from json import dump, load
from os.path import abspath, dirname, join
from pathlib import Path
from random import SystemRandom

BASEDIR = abspath(dirname(__file__))
CONFIG = Path(join(BASEDIR, "config.json"))

if CONFIG.is_file():
    conf = load(open(str(CONFIG)))
else:
    skey = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    conf = {"db_type": "sqlite", "secret_key": skey}
    dump(conf, open(str(CONFIG), 'w'))

if conf['db_type'] == "sqlite":
    DB = Path(join(BASEDIR, "database.db"))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(DB)
else:
    raise KeyError("db_type not defined in the config!")

SECRET_KEY = conf['secret_key']
WTF_CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

LIBRARY = Path(join(BASEDIR, "toshokan", "static", "manga"))

RESIZE_ROOT = "E:/Projects/Web/toshokan/toshokan/"
RESIZE_URL = "http://127.0.0.1:5000"
RESIZE_CACHE_DIR = ".thumbs"
