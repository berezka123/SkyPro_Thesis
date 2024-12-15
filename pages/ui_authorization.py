from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Authorization:
    """
        Класс содержит методы для авторизации на сайте Кинопоиска.
    """

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()

    def find_enter(self):
        """
            Метод реализует поиск кнопки Войти.
        """
        try:  # Закрыть коммуникацию.
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".styles_root__EjoL7").click()
        except NoSuchElementException:
            pass

        self._driver.find_element(By.CSS_SELECTOR,
                                  ".styles_loginButton__LWZQp").click()

    def authorization(self, timeout: int, username: str, password: str):
        """
            Метод реализует заполнение полей Логин или email,
        нажатие кнопки Войти, ввод пароля и нажатие кнопки Продолжить.
        """
        self._driver.implicitly_wait(timeout)
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').\
            send_keys(password)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        try:
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".Button2_view_contrast-pseudo").click()
        except NoSuchElementException:
            pass

    def incorrect_login(self, timeout: int, username: str):
        """
            Метод реализует заполнение полей Логин или email
        невалидными значениями.
        """
        self._driver.implicitly_wait(timeout)
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        message = self._driver.\
            find_element(By.XPATH, '//*[@id="field:input-login:hint"]').text
        return message
