import datetime


class Movie:
    """Movie Class"""

    def __init__(self, title: str, description: str, duration_in_mins: int, language: str, release_date: datetime.date, country: str, genre: str):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre

        self.__shows = []

    def get_shows(self, ):
        pass
