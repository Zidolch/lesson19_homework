from dao.model.genre import Genre


class GenreDAO:
    """
    Объект доступа к данным жанров
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Метод для получения одного жанра
        """
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """
        Метод для получения всех жанров
        """
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """
        Метод для добавления жанра в базу данных
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Метод для удаления жанра из базы данных
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """
        Метод для обновления информации о жанре
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
