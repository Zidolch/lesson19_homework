import calendar
import datetime
from constants import SECRET_KEY, ALGORYTHM, TOKEN_EXPIRE_MINUTES, TOKEN_EXPIRE_DAYS
import jwt
from flask_restx import abort
from service.user import UserService


class AuthService:
    """
    Сервис для работы с аутентификацией
    """
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        """
        Метод для создания токенов
        """
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not is_refresh:
            print(user.password)
            print(password)
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min_exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
        data["exp"] = calendar.timegm(min_exp.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, ALGORYTHM)

        days_exp = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
        data["exp"] = calendar.timegm(days_exp.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORYTHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """
        Метод для обновления токенов
        """
        data = jwt.decode(refresh_token, SECRET_KEY, [ALGORYTHM])
        username = data.get("username")

        return self.generate_tokens(username, None, is_refresh=True)
