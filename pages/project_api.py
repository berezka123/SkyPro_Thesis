import requests
import allure


class ProjectAPI:
    """
    Класс содержит методы, выполняющие HTTP-запросы к API Кинопоиска.
    """

    def __init__(self, url):
        self.url = url

    @allure.step("Универсальный поиск с фильтрами")
    def get_movies(self, filtres: dict = {}, auth_token: str = ""):
        """
            Метод реализует Универсальный поиск с фильтрами.
        """
        response = requests.get(self.url + "v1.4/movie", params=filtres,
                                headers=auth_token)
        return response

    @allure.step("Поиск фильмов по названию")
    def get_movies_by_name(self, filtres: dict = {}, auth_token: str = ""):
        """
            Метод реализует Поиск фильмов по названию.
        """
        response = requests.get(self.url + "v1.4/movie/search",
                                params=filtres, headers=auth_token)
        return response
