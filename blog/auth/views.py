from flask import Blueprint, request, render_template, redirect, url_for, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from blog.models import User
from blog.models.database import db
import uuid
import hashlib
from blog.forms.user import RegistrationForm, UserBaseForm

auth_app = Blueprint("auth_app", __name__, url_prefix='/auth')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    form = UserBaseForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            form.username.errors.append("username already not exists!")
            return render_template("auth/login.html", form=form)

        password = form.password.data
        if not check_password(user.password, password):
            form.username.errors.append("password error")
            return render_template("auth/login.html", form=form)
    
        login_user(user)
        return redirect(url_for("article.render_articles"))
    return render_template("auth/login.html", form=form)


@auth_app.route("/register", methods=["GET", "POST"], endpoint="register")
def register():
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.password = hash_password(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info("Created user %s", user)
            login_user(user)
            return redirect(url_for("article.render_articles"))
    return render_template("auth/register.html", form=form, error=error)


@auth_app.route("/logout", endpoint="logout")
@login_required
def logout():
   logout_user()
   return redirect(url_for("article.render_articles"))


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 

__all__ = [
    "login_manager",
    "auth_app",
    "login_required",
]
