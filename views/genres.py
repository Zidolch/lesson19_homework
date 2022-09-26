from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    """
    Представление для всех жанров
    """
    @auth_required
    def get(self):
        """
        Метод для получения всех жанров
        """
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        Метод для добавления жанра в базу данных
        """
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    """
    Представление для одного жанра
    """
    @auth_required
    def get(self, rid):
        """
        Метод для получения одного жанра
        """
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        """
        Метод для обновления данных одного жанра
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        """
        Метод для удаления одного жанра
        """
        genre_service.delete(rid)
        return "", 204
