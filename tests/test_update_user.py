import allure

import data
from endpoints.user_api import UserApi
import helpers


class TestUpdateUser:
    @allure.title('Обновление авторизованного пользователя')
    @allure.description('Проверка возможности обновления данных пользователя. Проверка статус и тело ответа')
    def test_update_authorized_user_success(self, get_default_user):
        login_body = helpers.get_login_user_data(get_default_user)
        response_login_user = UserApi.login_user(login_body)
        token = response_login_user.json()['accessToken']
        update_body = data.UPDATE_USER_BODY
        response_update_user = UserApi.update_user(token, update_body)

        assert (
            response_update_user.status_code == 200
            and response_update_user.json()['success'] is True
            and response_update_user.json()['user']['email'] == data.UPDATE_USER_BODY.get('email')
            and response_update_user.json()['user']['name'] == data.UPDATE_USER_BODY.get('name')
        )

    @allure.title('Обновление неавторизованного пользователя')
    @allure.description('Проверка невозможности обновления данных неавторизованного пользователя.'
                        'Проверка статуса и тело ответа')
    def test_update_unauthorized_user_unauthorized(self):
        token = ""
        update_body = data.UPDATE_USER_BODY
        response_update_user = UserApi.update_user(token, update_body)

        assert (
            response_update_user.status_code == 401
            and response_update_user.json()['success'] is False
            and response_update_user.json()['message'] == data.UNAUTHORIZED_ERROR
        )

    @allure.title('Обновление авторизованного пользователя. Изменение email на уже существующий в системе')
    @allure.description('Проверка невозможности обновления данных пользователя при изменении email на уже существующий'
                        'Проверка статуса и тело ответа')
    def test_update_auth_user_mail_of_already_registered_user(self, get_default_update_user):
        response_update_user = UserApi.update_user_mail_of_already_registered_user(get_default_update_user)

        assert (
            response_update_user.status_code == 403
            and response_update_user.json()['success'] is False
            and response_update_user.json()['message'] == data.SUCH_EMAIL_ALREADY_EXISTS
        )