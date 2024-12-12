# SkyPro_Thesis
Дипломная работа - Автоматизация тестирования на Python

## Задача проекта
Автоматизировать UI- и API-тесты из финальной работы по ручному тестированию.

## Структура проекта
 - каталог `pages`:
   - файл `__init__.py` необходим для того, чтобы Python воспринимал каталоги, содержащие этот файл, как пакеты;
   - файл `project_api.py` содержит методы для HTTP-запросов;
 - каталог `test`:
   - файл `__init__.py` необходим для того, чтобы Python воспринимал каталоги, содержащие этот файл, как пакеты;
   - файл `test_ui.py` содержит UI-тесты;
   - файл `test_api.py` содержит API-тесты.
 - файл `requirements.txt` содержит список всех необходимых библиотек и их версий, которые требуются для работы проекта.

## Запуск тестов

### Подготовка к запуску
Необходимо установить зависимости командой
`pip install -r requirements.txt`

### Запуск
запуск осуществляется командой:
`pytest .\test\test_api.py`
