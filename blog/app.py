from flask import Flask
from blog.users.views import user
from blog.home.views import home
from blog.articles.views import article
from blog.auth.views import auth_app

from blog.auth.views import login_manager
from blog.config import config_add

from blog.models.database import db
from flask_wtf.csrf import CSRFProtect


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    config_add(app)
    register_blueprints(app)
    
    register_database(app)
    migrate = Migrate(app, db)

    register_login_manager(app)

    csrf.init_app(app)
    
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(home)
    app.register_blueprint(article)
    app.register_blueprint(auth_app)


def register_database(app: Flask):
    db.init_app(app)


def register_login_manager(app: Flask):
    login_manager.login_view = "auth_app.login"
    login_manager.init_app(app)
