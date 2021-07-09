from blog import models
from blog.app import admin
from blog.models.database import db

from blog.admin.views import TagAdminView, CustomView


admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Articles, db.session, category="Models"))
