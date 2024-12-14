from pages.ui_authorization import Authorization
from pages.ui_search import Search
from selenium import webdriver
from time import sleep


def test_kinopoisk_auth():
    username = "example@yandex.ru"
    password = "P@ssW0rd"
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    sleep(60)  # Это время на решение капчи.
    
    authorization_page.find_enter()
    authorization_page.authorization(3, username, password)
    sleep(60)
    browser.quit()

def test_kinopoisk_search():
    query = "Заговор сестёр Гарви"
    browser = webdriver.Chrome()

    search_page = Search(browser)
    sleep(60)  # Это время на решение капчи.

    result = search_page.search_query(query)
    assert result == query
    sleep(60)
    browser.quit()