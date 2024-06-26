import pytest

from data import REGISTER_USER_BODY
from endpoints.user_api import UserApi
from helpers import get_login_user_data


@pytest.fixture(scope='function')
def get_default_user():
    payload = REGISTER_USER_BODY

    yield payload

    response = UserApi.login_user(payload)
    if response.status_code == 200:
        token = response.json()['accessToken']
        UserApi.delete_user(token)
    else:
        pass


# Фикстура - получение токена авторизации после регистрации и авторизации рандомного пользователя
@pytest.fixture(scope='function')
def get_default_update_user(get_default_user):
    login_body = get_login_user_data(get_default_user)
    response_login_user = UserApi.login_user(login_body)
    token = response_login_user.json()['accessToken']

    yield token
