from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from blog.api.article import ArticleList, ArticleDetail, ArticleRelationship

from combojsonapi.spec import ApiSpecPlugin

def create_api_spec_plugin(app):
     api_spec_plugin = ApiSpecPlugin(
         app=app,
         # Declaring tags list with their descriptions,
         # so API gets organized into groups. it's optional.
         tags={
             "Tag": "Tag API",
             "Articles": "Articles API"
         }
     )
     return api_spec_plugin


def init_api(app):
     api_spec_plugin = create_api_spec_plugin(app)
     api = Api(
         app,
         plugins=[
             api_spec_plugin,
         ],
     )


     api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
     api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
     api.route(ArticleList, "article_list", "/api/articles/", tag="Articles")
     api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>/", tag="Articles")
     api.route(ArticleRelationship, "article_relationship", "/api/articles/<int:id>/tags", tag="Articles")
