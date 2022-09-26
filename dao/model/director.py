from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    """
    Модель режиссера
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Схема для сериализации данных режиссера
    """
    id = fields.Int()
    name = fields.Str()
