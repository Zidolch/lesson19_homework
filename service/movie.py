from dao.movie import MovieDAO


class MovieService:
    """
    Сервис для работы с фильмами
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Метод для получения одного фильма
        """
        return self.dao.get_one(bid)

    def get_all(self, filters):
        """
        Метод для получения всех фильмов по выбранным параметрам
        """
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        """
        Метод для добавления фильма в базу данных
        """
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """
        Метод для обновления информации о фильме
        """
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        """
        Метод для удаления фильма из базы данных
        """
        self.dao.delete(rid)
