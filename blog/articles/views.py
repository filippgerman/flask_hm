from flask import Blueprint, render_template, request, redirect, url_for
from blog.models import Articles, ArticleTags, Tag
from blog.auth.views import login_required, current_user
from blog.models.database import db



from blog.forms.article import CreateArticleForm
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


@article.route('/<string:tag_name>')
def get_articles_tag(tag_name: str):
    tag = Tag.query.filter(Tag.name== tag_name).first()
    return render_template("articles/tagArticles.html", article=tag)

    
@article.route('/create', methods=["GET", "POST"])
@login_required
def create():
    form = CreateArticleForm(request.form)
    tags = Tag.query.all()
    if request.method == "POST":
        
        article_post = Articles(
            title = form.title.data,
            text = form.text.data,
            author_id = current_user.id
        )
        db.session.add(article_post)
        db.session.commit()
        
        if tags_post := request.form.getlist('tags_article'):
            tags = Tag.query.filter(Tag.name.in_(tags_post))
            for tag in tags:
                link = ArticleTags(article_id=article_post.id, tag_id=tag.id)
                db.session.add(link)
                db.session.commit()
        return redirect(url_for("article.render_articles"))
    return render_template("articles/create.html", form=form, tags=tags)

    
