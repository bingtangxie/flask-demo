from . import BaseModel
from apps import db


class Students(BaseModel, db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
