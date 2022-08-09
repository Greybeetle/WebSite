# app/exts.py  插件模块
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()
login_manager = LoginManager()

