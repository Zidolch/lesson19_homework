from dao.genre import GenreDAO


class GenreService:
    """
    Сервис для работы с жанрами
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения одного жанра
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Метод для получения всех жанров
        """
        return self.dao.get_all()

    def create(self, genre_d):
        """
        Метод для добавления жанра в базу данных
        """
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """
        Метод для обновления информации о жанре
        """
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления жанра из базы данных
        """
        self.dao.delete(rid)
