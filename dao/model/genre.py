from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """
    Модель жанра
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """
    Схема для сериализации данных жанра
    """
    id = fields.Int()
    name = fields.Str()
