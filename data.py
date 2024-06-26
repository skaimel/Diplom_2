from faker import Faker

fake = Faker("ru_RU")

# Тела запросов для регистрации пользователей
REGISTER_USER_BODY = {
    "email": fake.email(),
    "password": fake.password(),
    "name": fake.name()
}

REGISTER_USER_BODY_WITHOUT_EMAIL = {
    "password": fake.password(),
    "name": fake.name()
}

REGISTER_USER_BODY_WITH_EMPTY_EMAIL = {
    "email": "",
    "password": fake.password(),
    "name": fake.name()
}

REGISTER_USER_BODY_WITHOUT_PASSWORD = {
    "email": fake.email(),
    "name": fake.name()
}

REGISTER_USER_BODY_WITH_EMPTY_PASSWORD = {
    "email": fake.email(),
    "password": "",
    "name": fake.name()
}

REGISTER_USER_BODY_WITHOUT_NAME = {
    "email": fake.email(),
    "password": fake.password()
}

REGISTER_USER_BODY_WITH_EMPTY_NAME = {
    "email": fake.email(),
    "password": fake.password(),
    "name": ""
}

# Тело запроса для обновления данных пользователя - только name
UPDATE_USER_BODY = {
    "email": fake.email(),
    "name": fake.name()
}

# Данные для входа уже зарегистрированного пользователя
LOGIN_PASS_ALREADY_REGISTERED_USER = {
    "email": 'Slava_Melman_8_008@yandex.ru',
    "password": '123456'
}

# Данные для создания заказа
CREATE_ORDER_BODY = {
    'ingredients': ["61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa6d"]
}

# Данные для проверки созданного заказа
CREATE_ORDER_NAME = 'Метеоритный флюоресцентный традиционный-галактический бургер'

# Данные для создания заказа с недопустимыми ингредиентами
CREATE_ORDER_WITH_INVALID_INGREDIENTS_BODY = {
    'ingredients': ['61c0c5a71d1f82001bdaaa744', '61c0c5a71d1f82001bdaaa707']
}

# Ответы с сервера
UNAUTHORIZED_ERROR = 'You should be authorised'
INTERNAL_SERVER_ERROR = 'Internal Server Error'
SUCH_EMAIL_ALREADY_EXISTS = 'User with such email already exists'
EMAIL_PASSWORD_INCORRECT = 'email or password are incorrect'
USER_ALREADY_EXISTS = 'User already exists'
ERROR_REQUIRED_FIELDS = 'Email, password and name are required fields'