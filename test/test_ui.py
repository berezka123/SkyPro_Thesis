import pytest
from pages.ui_authorization import Authorization
from pages.ui_search import Search
from selenium import webdriver
from time import sleep


def resolving_captcha():
    """
        Функция решения капчи.
    Принцип предельно прост: капчу решает человек.
        Не благодарите :)
    """
    sleep(60)


def test_kinopoisk_auth():
    username = "example@yandex.ru"
    password = "P@ssW0rd"
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha()

    authorization_page.find_enter()
    authorization_page.authorization(3, username, password)
    sleep(60)
    browser.quit()


@pytest.mark.parametrize("login", "alert",
                         [("", "Логин не указан"),
                          (" ", "Логин не указан"),
                          ("example@@yandex.ru", "Такой логин не подойдет"),
                          ("example@yandex", "Такой логин не подойдет"),
                          ("o'Brian@yandex.ru", "Такой логин не подойдет")
                          ])
def test_incorrect_login(login, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha()
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_login(3, login) == alert
    sleep(5)
    browser.quit()


@pytest.mark.parametrize("corect_query", ["Гарви",
                                          "Харви",
                                          "Fargo"])
def test_kinopoisk_correct_search(corect_query):
    browser = webdriver.Chrome()

    search_page = Search(browser)
    resolving_captcha()

    assert search_page.search_query(corect_query) != 0
    sleep(5)
    browser.quit()


@pytest.mark.parametrize("incorect_query", ["   ",
                                            "!@#$",
                                            "asdfghjklhqweyurgtyuiop"])
def test_kinopoisk_incorrect_search(incorect_query):
    browser = webdriver.Chrome()

    search_page = Search(browser)
    resolving_captcha()

    assert search_page.search_query(incorect_query) == 0
    sleep(5)
    browser.quit()
