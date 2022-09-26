import base64
import hmac

from dao.user import UserDAO
import hashlib
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    """
    Сервис для работы с пользователями
    """
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения одного пользователя
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Метод для получения всех пользователей
        """
        return self.dao.get_all()

    def get_by_username(self, username):
        """
        Метод для получения пользователя по имени
        """
        return self.dao.get_by_username(username)

    def create(self, user_d):
        """
        Метод для добавления пользователя в базу данных
        """
        user_d["password"] = self.make_user_password_hash(user_d.get("password"))
        return self.dao.create(user_d)

    def update(self, user_d):
        """
        Метод для обновления информации о пользователе
        """
        user_d["password"] = self.make_user_password_hash(user_d.get("password"))
        self.dao.update(user_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления пользователя из базы данных
        """
        self.dao.delete(rid)

    def make_user_password_hash(self, password):
        """
        Метод для хеширования пароля пользователя
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password):
        """
        Метод для проверки пароля пользователя
        """
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)
