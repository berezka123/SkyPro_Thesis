import test
import allure
import pytest
from selenium import webdriver
from pages.ui_captcha import CaptchaResolve
from pages.ui_authorization import Authorization
from pages.ui_search import Search


@allure.title("Автотест на авторизацию по Логину или e-mail")
@allure.description("Негативный тест-кейс на ввод некорректного Логина\
                     или e-mail")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("login, alert",
                         [("", "Логин не указан"),
                          (" ", "Логин не указан"),
                          ("example@@yandex.ru", "Такой логин не подойдет"),
                          ("example@yandex", "Такой логин не подойдет"),
                          ("o'Brian@yandex.ru", "Такой логин не подойдет")
                          ])
def test_incorrect_login(login, alert):
    browser = webdriver.Firefox()

    authorization_page = Authorization(browser)
    captcha_resolver = CaptchaResolve(browser)
    captcha_resolver.resolving_captcha()
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_login(3, login) == alert

    browser.quit()


@allure.title("Автотест на авторизацию по Логину или e-mail")
@allure.description("Негативный тест-кейс на ввод некорректного Пароля")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("login, password, alert",
                         [(test.correct_login, "", "Пароль не указан"),
                          (test.correct_login, " ", "Пароль не указан"),
                          (test.correct_login, "asd123", "Неверный пароль"),
                          (test.correct_login, "\n\r\t", "Пароль не указан")
                          ])
def test_incorrect_password(login, password, alert):
    browser = webdriver.Firefox()

    authorization_page = Authorization(browser)
    captcha_resolver = CaptchaResolve(browser)
    captcha_resolver.resolving_captcha()
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_password(3, login, password) == alert

    browser.quit()


@allure.title("Автотест на авторизацию по Телефону")
@allure.description("Негативный тест-кейс на ввод некорректного Телефона")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("phone, alert",
                         [("", "Недопустимый формат номера"),
                          ("98765432101234", "Недопустимый формат номера")
                          ])
def test_incorrect_phone(phone, alert):
    browser = webdriver.Firefox()

    authorization_page = Authorization(browser)
    captcha_resolver = CaptchaResolve(browser)
    captcha_resolver.resolving_captcha()
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_phone(3, phone) == alert

    browser.quit()


@allure.title("Автотест на Поиск")
@allure.description("Позитивный тест-кейс на поиск по корректному запросу")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("corect_query", ["Гарви",
                                          "Леонардо ди Каприо",
                                          "Fargo"])
def test_kinopoisk_correct_search(corect_query):
    browser = webdriver.Firefox()

    search_page = Search(browser)
    captcha_resolver = CaptchaResolve(browser)
    captcha_resolver.resolving_captcha()
    assert search_page.search_query(corect_query) != 0

    browser.quit()


@allure.title("Автотест на Поиск")
@allure.description("Негативный тест-кейс на поиск по некорректному запросу")
@allure.feature("Поиск")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("incorect_query", ["   ",
                                            "!@#$",
                                            "asdfghjklhqweyurgtyuiop"])
def test_kinopoisk_incorrect_search(incorect_query):
    browser = webdriver.Firefox()

    search_page = Search(browser)
    captcha_resolver = CaptchaResolve(browser)
    captcha_resolver.resolving_captcha()
    assert search_page.search_query(incorect_query) == 0

    browser.quit()
