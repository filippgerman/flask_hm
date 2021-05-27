from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from blog.models import User
from blog.models.database import db
import uuid
import hashlib


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
    if request.method == "GET":
        return render_template("auth/login.html")

    username = request.form.get("username")
    if not username:
        return render_template("auth/login.html", error="username not passed")

    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"no user {username!r} found")

    password = request.form.get("password")
    if not check_password(user.password, password):
        return render_template("auth/login.html", error=f"password error")
    
    login_user(user)
    return redirect(url_for("article.render_articles"))


@auth_app.route("/registration", methods=["GET", "POST"], endpoint="registration")
def registration():
    if request.method == "GET":
        return render_template("auth/registration.html")

    form_username = request.form.get("username")
    check_user = User.query.filter_by(username=form_username).one_or_none()
    if check_user is not None:
        return render_template("auth/registration.html", error=f"this nickname {username!r} is busy")
    
    form_email = request.form.get("email")
    check_email = User.query.filter_by(email=form_email).one_or_none()
    if check_email is not None:
        return render_template("auth/registration.html", error=f"this email is busy")
    
    form_password = request.form.get("password")
    form_password_hash = hash_password(form_password)

    user = User(username=form_username,
                password=form_password_hash,
                email=form_email)

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email=form_email).one_or_none()
    login_user(user)
    return redirect(url_for("article.render_articles"))
    

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
