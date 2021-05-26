from flask import Blueprint, render_template
from blog.models import Articles
from blog.auth.views import login_required

article = Blueprint('article', __name__, url_prefix='/articles')


@article.route('/')
def render_articles():
    articles_list = Articles.query.all()
    return render_template("articles/index.html", articles=articles_list)


@article.route('/<int:pk>')
@login_required
def get_articles(pk: int):
    result = Articles.query.filter(Articles.id == pk).first()
    return render_template("articles/article.html", article=result)
    
