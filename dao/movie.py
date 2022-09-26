from dao.model.movie import Movie


class MovieDAO:
    """
    Объект доступа к данным фильмов
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Метод для получения одного фильма
        """
        return self.session.query(Movie).get(bid)

    def get_all(self):
        """
        Метод для получения всех фильмов
        """
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        """
        Метод для получения всех фильмов по выбранному режиссеру
        """
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        """
        Метод для получения всех фильмов по выбранному жанру
        """
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        """
        Метод для получения всех фильмов по выбранному году
        """
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        """
        Метод для добавления фильма в базу данных
        """
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Метод для удаления фильма из базы данных
        """
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        """
        Метод для обновления информации о фильме
        """
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
