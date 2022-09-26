from flask_restx import Resource, Namespace
from flask import request
from dao.model.user import UserSchema
from implemented import user_service
from service.decorators import admin_required

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    """
    Представление для всех пользователей
    """
    @admin_required
    def get(self):
        """
        Метод для получения всех пользователей
        """
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        """
        Метод для добавления пользователя в базу данных
        """
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:rid>')
class UserView(Resource):
    """
    Представление для одного пользователя
    """
    @admin_required
    def get(self, rid):
        """
        Метод для получения одного пользователя
        """
        r = user_service.get_one(rid)
        sm_u = UserSchema().dump(r)
        return sm_u, 200

    @admin_required
    def put(self, rid):
        """
        Метод для обновления данных одного пользователя
        """
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        user_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        """
        Метод для удаления одного пользователя
        """
        user_service.delete(rid)
        return "", 204