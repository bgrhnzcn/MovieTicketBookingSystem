from abc import ABC
import sqlite3 as sql
import datetime


class Movie:
    """Movie Class"""
    __id = 0

    def __init__(self, title: str, description: str, duration_in_mins: int, language: str, release_date: datetime.date,
                 country: str, genre: str):
        Movie.__id = Movie.__id + 1
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre
        self.__movie_data = (Movie.__id, self.__title, self.__description,
                             self.__duration_in_mins, self.__language, self.__release_date, self.__country, self.__genre)
        conn = sql.connect("example_database.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO 'MOVIES'
                        ('id','title','description','durationinmins','language','releasedate','country','genre')
                         VALUES (?,?,?,?,?,?,?,?);""", self.__movie_data)
        conn.commit()
        conn.close()
        self.__shows = []

    def __del__(self):
        conn = sql.connect("example_database.db")
        cursor = conn.cursor()
        cursor.execute("""""")
        conn.commit()
        conn.close()

    def get_shows(self):
        pass


class Search(ABC):

    def search_by_title(self):
        pass

    def search_by_language(self):
        pass

    def search_by_genre(self):
        pass

    def search_by_release_date(self):
        pass

    def search_by_city(self):
        pass


class Catalogue(Search):

    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

    def search_by_title(self, title):
        print("Hello")
        return self.__movie_titles.get(title)


movie1 = Movie("Film", "Tanım", 55, "Türkçe", datetime.date.today(), "Türkiye", "Korku")
movie2 = Movie("Film", "Tanım", 55, "Türkçe", datetime.date.today(), "Türkiye", "Korku")
movie3 = Movie("Film", "Tanım", 55, "Türkçe", datetime.date.today(), "Türkiye", "Korku")



