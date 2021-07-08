from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey, Table
from blog.models.database import db
from datetime import datetime
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Articles(db.Model):
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    text = Column(Text, nullable=False)
    date_create = Column(DateTime, default=datetime.utcnow())
    
    author_id = Column(Integer, db.ForeignKey('User.id'), nullable=False)
    tags = relationship("Tag",
                        secondary="ArticleTags")
    
    def __repr__(self):
        return f"Article {self.title}"


class Tag(db.Model):
    __tablename__ = "Tag"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    articles = relationship("Articles",
                            secondary="ArticleTags")

    def __repr__(self):
        return f"Tag {self.name}"


class ArticleTags(db.Model):
    __tablename__ = 'ArticleTags'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('Articles.id'))
    tag_id = Column(Integer, ForeignKey('Tag.id'))

    tags = relationship(Tag, backref=backref("ArticleTags",
                                             cascade="all, delete-orphan",
                                             lazy='dynamic'))
    article  = relationship(Articles, backref=backref("ArticleTags",
                                                      cascade="all, delete-orphan",
                                                      lazy='dynamic'))
    
    def __repr__(self):
        return f"link {self.article_id} {self.tag_id}"



