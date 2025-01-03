import test
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Authorization:
    """
        Класс содержит методы для авторизации на сайте Кинопоиска.
    """

    def __init__(self, browser):
        self._driver = browser
        self._driver.get(test.url)
        self._driver.maximize_window()

    @allure.step("Поиск кнопки Войти и её нажатие")
    def find_enter(self) -> None:
        """
            Метод реализует поиск кнопки Войти и её нажатие.
        """
        try:  # Закрыть коммуникацию.
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".styles_root__EjoL7").click()
        except NoSuchElementException:
            pass

        self._driver.find_element(By.CSS_SELECTOR,
                                  ".styles_loginButton__LWZQp").click()

    @allure.step("Авторизация с логином {username} и паролем {password}")
    def authorization(self, timeout: int, username: str, password: str)\
            -> None:
        """
            Метод реализует заполнение поля Логин или email,
        нажатие кнопки Войти, ввод пароля и нажатие кнопки Продолжить.
        """
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="passp-field-passwd"]')
            )
        )
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').\
            send_keys(password)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        try:
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".Button2_view_contrast-pseudo").click()
        except NoSuchElementException:
            pass

    @allure.step("Заполнение поля Логин или email невалидным значением\
                 {username}")
    def incorrect_login(self, timeout: int, username: str) -> str:
        """
            Метод реализует заполнение поля Логин или email (подразумевается
        заполнение поля невалидным значением) и возвращает текст сообщения
        об ошибке.
        """
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="field:input-login:hint"]')
            )
        )
        message = self._driver.\
            find_element(By.XPATH, '//*[@id="field:input-login:hint"]').text
        return message

    @allure.step("Заполнение поля Пароль невалидным значением\
                 {password}")
    def incorrect_password(self, timeout: int, username: str, password: str)\
            -> str:
        """
            Метод реализует заполнение поля Логин или email,
        нажатие кнопки Войти, и заполнение поля Пароль (подразумевается
        заполнение поля невалидным значением) и возвращает текст сообщения
        об ошибке.
        """
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="passp-field-passwd"]')
            )
        )
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').\
            send_keys(password)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="field:input-passwd:hint"]')
            )
        )
        message = self._driver.\
            find_element(By.XPATH, '//*[@id="field:input-passwd:hint"]').text
        return message

    @allure.step("Заполнение поля Телефон невалидным значением\
                 {phone}")
    def incorrect_phone(self, timeout: int, phone: str) -> str:
        """
            Метод реализует переключение на вход по номеру телефона,
        заполнение поля Телефон (подразумевается заполнение поля невалидным
        значением) и возвращает текст сообщения об ошибке.
        """
        self._driver.find_element(By.CSS_SELECTOR, '.Button2_view_clear').\
            click()
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-phone"]').\
            send_keys(phone)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="field:input-phone:hint"]')
            )
        )
        message = self._driver.\
            find_element(By.XPATH, '//*[@id="field:input-phone:hint"]').text
        return message
