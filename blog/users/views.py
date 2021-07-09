from flask import Blueprint, render_template
from blog.models import User, Articles
from blog.auth.views import login_required

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/')
@login_required
def user_list():
    names_list = User.query.all()
    return render_template("users/index.html", names=names_list)

@user.route('/<int:pk>')
@login_required
def details(pk:int):
    result = Articles.query.filter(Articles.author_id == pk).all()
    return render_template("users/details.html", data=result)
