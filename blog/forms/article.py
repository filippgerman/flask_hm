from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField

class CreateArticleForm(FlaskForm):
    title = StringField("title", [validators.DataRequired()],)
    text = StringField("text", [validators.DataRequired()],)

