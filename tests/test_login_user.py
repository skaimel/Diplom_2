import allure

import data
import helpers
from endpoints.user_api import UserApi


class TestLoginUser:
    @allure.title('Успешный логин пользователя')
    @allure.description('Проверка успешного логина пользователя. Проверка статуса и тело ответа')
    def test_login_user_success(self, get_default_user):
        body = helpers.get_login_user_data(get_default_user)
        response_login_user = UserApi.login_user(body)

        assert (
            response_login_user.status_code == 200
            and response_login_user.json()['success'] is True
            and response_login_user.json()["user"] is not None
        )

    @allure.title('Невозможность логина пользователя с невалидным email')
    @allure.description('Проверка невозможности логина пользователя, если email неверный.'
                        'Проверка статуса и тело ответа')
    def test_login_user_with_invalid_email_unauthorized(self, get_default_user):
        body = helpers.get_login_request_with_invalid_email(get_default_user)
        response_login_user = UserApi.login_user(body)

        assert (
            response_login_user.status_code == 401
            and response_login_user.json()['success'] is False
            and response_login_user.json()["message"] == data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Невозможность логина пользователя с невалидным password')
    @allure.description('Проверка невозможности логина пользователя, если password неверный.'
                        'Проверка статуса и тело ответа')
    def test_login_user_with_invalid_password_unauthorized(self, get_default_user):
        body = helpers.get_login_request_with_invalid_password(get_default_user)
        response_login_user = UserApi.login_user(body)

        assert (
            response_login_user.status_code == 401
            and response_login_user.json()['success'] is False
            and response_login_user.json()["message"] == data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Невозможность логина пользователя без email')
    @allure.description('Проверка невозможности логина пользователя, если email отсутствует в теле запроса.'
                        'Проверка статуса и тело ответа')
    def test_login_user_without_email_unauthorized(self, get_default_user):
        body = helpers.get_login_request_without_email(get_default_user)
        response_login_user = UserApi.login_user(body)

        assert (
            response_login_user.status_code == 401
            and response_login_user.json()['success'] is False
            and response_login_user.json()["message"] == data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Невозможность логина пользователя без password')
    @allure.description('Проверка невозможности логина пользователя, если password отсутствует в теле запроса.'
                        'Проверка статуса и тело ответа')
    def test_login_user_without_password_unauthorized(self, get_default_user):
        body = helpers.get_login_request_without_password(get_default_user)
        response_login_user = UserApi.login_user(body)

        assert (
            response_login_user.status_code == 401
            and response_login_user.json()['success'] is False
            and response_login_user.json()["message"] == data.EMAIL_PASSWORD_INCORRECT
        )