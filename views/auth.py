from flask_restx import Resource, Namespace, abort
from flask import request

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    """
    Представление для аутентификации пользователя
    """
    def post(self):
        """
        Метод для получения токенов
        """
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")

        if not username or not password:
            abort(400)

        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        """
        Метод для обновления токенов
        """
        req_json = request.json
        refresh_token = req_json.get("refresh_token")

        if not refresh_token:
            abort(400)

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
