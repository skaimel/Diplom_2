# Базовый URL для API
BASE_URL = 'https://stellarburgers.nomoreparties.site'

# Эндпоинты для пользователя
USER_ENDPOINTS = {
    'REGISTER': '/api/auth/register',  # Регистрация пользователя POST
    'LOGIN': '/api/auth/login',  # Авторизация пользователя POST
    'DELETE': '/api/auth/user',  # Удаление пользователя DELETE
    'GET': '/api/auth/user',  # Получение данных о пользователе GET
    'PATCH': '/api/auth/user',  # Обновление данных о пользователе PATCH
    'LOGOUT': '/api/auth/logout'  # Выход из системы POST
}

# Эндпоинты для заказов
ORDER_ENDPOINTS = {
    'CREATE_ORDER': '/api/orders',  # Создание заказа POST
    'GET_ORDERS': '/api/orders'  # Получение заказов GET
}