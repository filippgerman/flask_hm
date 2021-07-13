from flask import Flask

from blog.auth.views import login_manager
from blog.config import config_add

from blog.models.database import db
from flask_wtf.csrf import CSRFProtect

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin
from blog.admin.views import MyAdminIndexView

from blog.api import init_api

csrf = CSRFProtect()
admin = Admin(name="Blog Admin",index_view=MyAdminIndexView(), template_mode="bootstrap4")



def create_app():
    app = Flask(__name__)
    config_add(app)
    
    register_blueprints(app)
    register_database(app)
    
    register_login_manager(app)

    admin.init_app(app)
    csrf.init_app(app)
    api = init_api(app)
    
    return app

def register_blueprints(app: Flask):
    from blog.users.views import user
    from blog.home.views import home
    from blog.articles.views import article
    from blog.auth.views import auth_app
    from blog.admin.views import admin_dp
    
    app.register_blueprint(user)
    app.register_blueprint(home)
    app.register_blueprint(article)
    app.register_blueprint(auth_app)
    app.register_blueprint(admin_dp)

def register_database(app: Flask):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_login_manager(app: Flask):
    login_manager.login_view = "auth_app.login"
    login_manager.init_app(app)
