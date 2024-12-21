import test
import allure
from pages.project_api import ProjectAPI


api_key = {
    "X-API-KEY": f"{test.x_api_key}"
}

kinopoisk = ProjectAPI(test.base_url)


@allure.title("Автотест на Универсальный поиск")
@allure.description("Позититвный тест-кейс на поиск по высокому рейтингу")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_rating(filtres={"rating.kp": "9.1-10"},
                              auth_token=api_key):
    """
        POS Поиск по высокому рейтингу Кинопоиск.
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на Универсальный поиск")
@allure.description("Позититвный тест-кейс на поиск по наличию билетов в\
                     продаже, возрастному рейтингу и типу фильма")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_ticket(filtres={"ticketsOnSale": "true",
                                       "ageRating": "0-12",
                                       "type": "movie"},
                              auth_token=api_key):
    """
        POS Поиск по наличию билетов в продаже, возрастному рейтингу
    и типу фильма.
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на Универсальный поиск")
@allure.description("Позититвный тест-кейс на поиск по жанру и возрастному\
                     рейтингу")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_genre(filtres={"genres.name": "драма",
                                      "ageRating": "18"},
                             auth_token=api_key):
    """
        POS Поиск по жанру и возрастному рейтингу
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на Поиск фильмов по названию")
@allure.description("Позититвный тест-кейс на поиск по названию")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_name(filtres={"query": "Три кота"},
                            auth_token=api_key):
    """
        POS Поиск по названию
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на Поиск фильмов по названию")
@allure.description("Позититвный тест-кейс на поиск по названию с опечатками")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_name_with_opechatka(filtres={"query": "татаник"},
                                           auth_token=api_key):
    """
        POS Поиск по названию с опечатками
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на Поиск фильмов по названию")
@allure.description("Негативный тест-кейс на поиск с отсутствием значений\
                     в поисковой строке")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_empty_name(filtres={"query": ""},
                                  auth_token=api_key):
    """
        NEG Поиск по пустому названию
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] == 0


@allure.title("Автотест на Поиск фильмов по названию")
@allure.description("Негативный тест-кейс на поиск по названию\
                     в неправильной раскладке")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_incorrect_name(filtres={"query": "Keynbr"},
                                      auth_token=api_key):
    """
        NEG Поиск по названию в неправильной раскладке
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] == 0
