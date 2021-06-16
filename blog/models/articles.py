from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from blog.models.database import db
from datetime import datetime
from sqlalchemy.orm import backref, relationship

class Articles(db.Model):
    __tablename__="Articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    text = Column(Text, nullable=False)
    date_create = Column(DateTime, default=datetime.utcnow())
    author_id = Column(Integer, db.ForeignKey('User.id'), nullable=False)
    
    def __repr__(self):
        return f"Article {self.title}"
