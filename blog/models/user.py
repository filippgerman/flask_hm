from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from sqlalchemy.orm import backref, relationship
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    articles = db.relationship('Articles', backref='user_articles', lazy=True)
    
    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
