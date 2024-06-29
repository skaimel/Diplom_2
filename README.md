Автотесты для проверки API сайта https://stellarburgers.nomoreparties.site


Структура

- `allure_results` - Allure отчет
- `tests` - директория с тестами


Установка зависимостей
> `$ pip install -r requirements.txt`

Запуск тестов
`pytest tests/ --alluredir=allure_results`

Запуск отчетности allure
`allure serve allure_results` 