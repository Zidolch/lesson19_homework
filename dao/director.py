from dao.model.director import Director


class DirectorDAO:
    """
    Объект доступа к данным режиссеров
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Метод для получения одного режиссеров
        """
        return self.session.query(Director).get(bid)

    def get_all(self):
        """
        Метод для получения всех режиссеров
        """
        return self.session.query(Director).all()

    def create(self, director_d):
        """
        Метод для добавления режиссера в базу данных
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Метод для удаления режиссера из базы данных
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """
        Метод для обновления информации о режиссере
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
