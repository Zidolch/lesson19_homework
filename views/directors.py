from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from implemented import director_service
from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Представление для всех режиссеров
    """
    @auth_required
    def get(self):
        """
        Метод для получения всех режиссеров
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """
        Метод для добавления режиссера в базу данных
        """
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    """
    Представление для одного режиссера
    """
    @auth_required
    def get(self, rid):
        """
        Метод для получения одного режиссера
        """
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        """
        Метод для обновления данных одного режиссера
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        """
        Метод для удаления одного режиссера
        """
        director_service.delete(rid)
        return "", 204
