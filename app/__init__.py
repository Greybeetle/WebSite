from flask import Flask
from . import auth, blog
from .exts import db, migrate, bootstrap, login_manager
from . import setting
from .model import User


# 应用工厂函数
def create_app():
    app = Flask(__name__)
    app.config.from_object(setting.Default)
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    return app
