from flask_combo_jsonapi import ResourceDetail, ResourceList, ResourceRelationship

from blog.schemas import ArticleSchema
from blog.models.database import db
from blog.models import Articles


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
    }

class ArticleRelationship(ResourceRelationship):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Articles,
    }
