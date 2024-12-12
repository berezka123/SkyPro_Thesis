import requests


class ProjectAPI:
    """
    Класс содержит методы, выполняющие HTTP-запросы к API Кинопоиска.
    """

    def __init__(self, url):
        self.url = url

    def get_movies(self, filtres=None, auth_token=None):
        """
            Метод реализует Универсальный поиск с фильтрами.
        """
        response = requests.get(self.url + "v1.4/movie", params=filtres,
                                headers=auth_token)
        return response

    def get_movies_by_name(self, filtres=None, auth_token=None):
        """
            Метод реализует Поиск фильмов по названию.
        """
        response = requests.get(self.url + "v1.4/movie/search",
                                params=filtres, headers=auth_token)
        return response
