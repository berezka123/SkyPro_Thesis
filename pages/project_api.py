import requests


class ProjectAPI:
    """
    Класс содержит методы, выполняющие HTTP-запросы к API Кинопоиска.
    """

    def __init__(self, url):
        self.url = url

    def get_movies(self, filtres=None, auth_token=None):
        response = requests.get(self.url + "movie", params=filtres, headers=auth_token)
        return response
