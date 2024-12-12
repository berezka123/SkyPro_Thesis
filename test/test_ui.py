from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#from pages.ui_authorization import Authorization

driver = webdriver.Chrome()
url = "https://www.kinopoisk.ru/"

# Переходим на страницу:
driver.get(url)

# Закрываем браузер:
driver.quit()