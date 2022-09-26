from dao.model.user import User


class UserDAO:
    """
    Объект доступа к данным пользователей
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Метод для получения одного пользователя
        """
        return self.session.query(User).get(bid)

    def get_all(self):
        """
        Метод для получения всех пользователей
        """
        return self.session.query(User).all()

    def get_by_username(self, username):
        """
        Метод для получения пользователя по имени
        """
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_d):
        """
        Метод для добавления пользователя в базу данных
        """
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Метод для удаления пользователя из базы данных
        """
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        Метод для обновления информации о пользователе
        """
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
