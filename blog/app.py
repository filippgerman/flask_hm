from flask import Flask
from blog.users.views import user
from blog.home.views import home
from blog.articles.views import article
from blog.auth.views import auth_app
from blog.models.database import db
from blog.auth.views import login_manager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdefg123456"
    register_blueprints(app)
    register_database(app)
    register_login_manager(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(home)
    app.register_blueprint(article)
    app.register_blueprint(auth_app)


def register_database(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://huston:fil@localhost/test_flask"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


def register_login_manager(app: Flask):
    login_manager.login_view = "auth_app.login"
    login_manager.init_app(app)
