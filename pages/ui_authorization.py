from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()
    
    def find_enter(self):
        self._driver.find_element(By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()

    def authorization(self, username, password):
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').\
            send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').\
            send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[id="login-button"]').click()
