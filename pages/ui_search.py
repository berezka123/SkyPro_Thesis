from selenium.webdriver.common.by import By


class Search:
    """
        Класс содержит методы для поиска фильмов, сериалов, персон.
    """

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()

    def search_query(self, query):
        """
            Метод реализует ввод поискового запроса.
        """
        try:  # Закрыть коммуникацию.
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".styles_root__EjoL7").click()
        except:
            pass
        self._driver.find_element(By.TAG_NAME,
                                  "input").send_keys(query)
        self._driver.find_element(By.CSS_SELECTOR,
                                  ".search-form-submit-button__icon").click()
        result = self._driver.find_elements(By.CSS_SELECTOR, ".styles-title___itJ6")
        return result