import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pages.ui_authorization import Authorization
from pages.ui_search import Search


def resolving_captcha(driver, timeout=60):
    """
        Функция решения капчи.
    В случае появления ----, автоматически отмечается чекбокс "Я не робот".
    В случае появления капчи, человеку нужно самостоятельно её решить за
    {timeout} (по умолчанию - 60) секунд.
    """
    try:  # Поставить галку "Я не робот".
        driver.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
    except NoSuchElementException:
        pass

    try:  # Закрыть коммуникацию.
        WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ".styles_root__EjoL7")
            )
        )
        driver.find_element(By.CSS_SELECTOR, ".styles_root__EjoL7").click()
    except TimeoutException:
        pass
    except NoSuchElementException:
        pass


@pytest.mark.parametrize("login, alert",
                         [("", "Логин не указан"),
                          (" ", "Логин не указан"),
                          ("example@@yandex.ru", "Такой логин не подойдет"),
                          ("example@yandex", "Такой логин не подойдет"),
                          ("o'Brian@yandex.ru", "Такой логин не подойдет")
                          ])
def test_incorrect_login(login, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha(browser)
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_login(3, login) == alert

    browser.quit()


@pytest.mark.parametrize("login, password, alert",
                         [("example@yandex.ru", "", "Пароль не указан"),
                          ("example@yandex.ru", " ", "Пароль не указан"),
                          ("example@yandex.ru", "asd123", "Неверный пароль"),
                          ("example@yandex.ru", "\n\t\r", "Неверный пароль"),
                          ("example@yandex.ru", "\033[2J", "Неверный пароль")
                          ])
def test_incorrect_password(login, password, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha(browser)
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_password(3, login, password) == alert

    browser.quit()


@pytest.mark.parametrize("phone, alert",
                         [("", "Недопустимый формат номера"),
                          ("98765432101234", "Недопустимый формат номера")
                          ])
def test_incorrect_phone(phone, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha(browser)
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_phone(3, phone) == alert

    browser.quit()


@pytest.mark.parametrize("corect_query", ["Гарви",
                                          "Харви",
                                          "Fargo"])
def test_kinopoisk_correct_search(corect_query):
#    browser = webdriver.Chrome()
    browser = webdriver.Firefox()

    search_page = Search(browser)
    resolving_captcha(browser)

    assert search_page.search_query(corect_query) != 0

    browser.quit()


@pytest.mark.parametrize("incorect_query", ["   ",
                                            "!@#$",
                                            "asdfghjklhqweyurgtyuiop"])
def test_kinopoisk_incorrect_search(incorect_query):
    browser = webdriver.Chrome()

    search_page = Search(browser)
    resolving_captcha(browser)

    assert search_page.search_query(incorect_query) == 0

    browser.quit()
