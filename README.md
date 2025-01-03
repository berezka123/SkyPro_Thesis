# SkyPro_Thesis
Дипломная работа - [Автоматизация тестирования на Python](https://github.com/berezka123/SkyPro_Thesis)

## Задача проекта
Автоматизировать UI- и API-тесты из финальной работы по ручному тестированию.

## Структура проекта
 - каталог `pages`:
   - файл `__init__.py` необходим для того, чтобы Python воспринимал каталоги, содержащие этот файл, как пакеты;
   - файл `project_api.py` содержит методы для HTTP-запросов;
   - файл `ui_captcha.py` содержит метод для решения SmartCaptcha[^1];
   - файл `ui_authorization.py` содержит методы для авторизации на сайте Кинопоиска;
   - файл `ui_search.py` содержит методы для поиска фильмов, сериалов, персон;
 - каталог `test`:
   - файл `__init__.py` необходим для того, чтобы Python воспринимал каталоги, содержащие этот файл, как пакеты; содержит специфичные данные (URL, токен, логин);
   - файл `test_ui.py` содержит UI-тесты;
   - файл `test_api.py` содержит API-тесты.
 - файл `requirements.txt` содержит список всех необходимых библиотек и их версий, которые требуются для работы проекта.

[^1]: Капча - тест, используется для определения, кем является пользователь: человеком или компьютером. В случае автоматизации тестирования, пользователем является компьютер, поэтому вполне закономерно появление капчи. Существуют способы автоматизированного решения капчи, но они платные. В проекте решение реализовано так - в случае появления сообщения "Подтвердите, что запросы отправляли вы, а не робот", автоматически отмечается чекбокс "Я не робот". В случае появления задания с картинкой, человеку нужно самостоятельно его решить.

## Запуск тестов

### Подготовка к запуску
Необходимо установить зависимости командой:
```
pip install -r requirements.txt
```
В файле `.\test\__init__.py` нужно указать специфичные данные:
- в переменную `x_api_key` нужно записать значение ключа, например:
```
x_api_key = "012ABC-345DEF-678GHI-9JKLNM"
```
- в переменную `correct_login` нужно записать логин Яндекс ID или адрес электронной почты Яндекс, например:
```
correct_login = "yandex_id"
```
или
```
correct_login = "example@yandex.ru"
```

**В UI-тестах используется Mozilla Firefox.**

### Запуск
Запуск всех тестов:
```
pytest .\test\
```

Запуск только UI-тестов:
```
pytest .\test\test_ui.py
```

Запуск только API-тестов:
```
pytest .\test\test_api.py
```

#### Запуск тестов с созданием отчётов Allure
Для создания отчётов Allure, необходимо запустить pytest с параметром `--alluredir` и указать путь к каталогу, в котором будут сохранены результаты тестирования, если такого каталога не существует, то он будет создан (не используйте заглавные буквы в пути - они будут проигнорированы).
Например:
```
pytest .\test\ --alluredir ..\..\allure-2.32.0\allure-result\test_skypro_thesis
```
