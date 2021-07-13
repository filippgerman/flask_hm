from flask import Blueprint, render_template, redirect, url_for
from blog.auth.views import login_required

from blog.models import Articles, ArticleTags, Tag

from flask_admin.contrib.sqla import ModelView

from flask_login import current_user
from flask_admin import Admin, AdminIndexView, expose


class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff
    
    def inaccessible_callback(self, name, **kwargs): 
        return redirect(url_for("auth.login"))


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth_app.login"))
        return super(MyAdminIndexView, self).index()

    
class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


class UserAdminView(CustomView):
    column_exclude_list = ("_password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False

    
admin_dp = Blueprint('admin_dp', __name__, url_prefix='/admin')
