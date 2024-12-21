import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class CaptchaResolve:
    """
        Класс содержит метод для решения SmartCaptha.
    """

    def __init__(self, browser):
        self._driver = browser

    @allure.step("Решение SmartCaptcha и закрытие окна с предложением\
                  подарка")
    def resolving_captcha(self, timeout: int = 60) -> None:
        """
            Метод решения SmartCaptha.
        В случае появления сообщения "Подтвердите, что запросы отправляли вы,
        а не робот", автоматически отмечается чекбокс "Я не робот".
        В случае появления задания с картинкой, человеку нужно самостоятельно
        её решить за {timeout} (по умолчанию - 60) секунд.
        """
        try:  # Поставить галку "Я не робот".
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".CheckboxCaptcha-Button").click()
        except NoSuchElementException:
            pass

        try:  # Закрыть коммуникацию.
            WebDriverWait(self._driver, timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, ".styles_root__EjoL7")
                )
            )
            self._driver.find_element(By.CSS_SELECTOR, ".styles_root__EjoL7")\
                .click()
        except TimeoutException:
            pass
        except NoSuchElementException:
            pass
