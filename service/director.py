from dao.director import DirectorDAO


class DirectorService:
    """
    Сервис для работы с режиссерами
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения одного режиссера
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Метод для получения всех режиссеров
        """
        return self.dao.get_all()

    def create(self, director_d):
        """
        Метод для добавления режиссера в базу данных
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        Метод для обновления информации о режиссере
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления режиссера из базы данных
        """
        self.dao.delete(rid)
