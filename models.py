from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()

class Advertisement(db.Model):
    __tablename__ = 'Advertisement'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    created_date = db.Column(DateTime(timezone=True), default=func.now())
    author = db.Column(db.String(80))

    def __init__(self, title, description, created_date,author):
        self.title = title
        self.description = description
        self.created_at = created_date
        self.author = author

    def json(self):
        return {"title": self.title, "description": self.description, "created_date": self.created_date,"author": self.author}