import allure
import requests

import urls
import data


class UserApi:
    @staticmethod
    @allure.step("Запрос на регистрацию пользователя")
    def register_user(body):
        return requests.post(urls.BASE_URL + urls.USER_ENDPOINTS['REGISTER'], json=body)

    @staticmethod
    @allure.step("Запрос на авторизацию пользователя")
    def login_user(body):
        return requests.post(urls.BASE_URL + urls.USER_ENDPOINTS['LOGIN'], json=body)

    @staticmethod
    @allure.step("Запрос на удаление пользователя")
    def delete_user(token):
        return requests.delete(urls.BASE_URL + urls.USER_ENDPOINTS['DELETE'], headers={'authorization': token})

    @staticmethod
    @allure.step("Запрос на получение данных пользователя")
    def get_user(token):
        return requests.get(urls.BASE_URL + urls.USER_ENDPOINTS['GET'], headers={'authorization': token})

    @staticmethod
    @allure.step("Запрос на обновление данных пользователя")
    def update_user(token, body):
        return requests.patch(urls.BASE_URL + urls.USER_ENDPOINTS['PATCH'], json=body,
                              headers={'authorization': token})

    @staticmethod
    @allure.step("Запрос на обновление данных пользователя уже имеющихся в системе (email)")
    def update_user_mail_of_already_registered_user(token):
        body = data.LOGIN_PASS_ALREADY_REGISTERED_USER
        return requests.patch(urls.BASE_URL + urls.USER_ENDPOINTS['PATCH'], json=body,
                              headers={'authorization': token})

    @staticmethod
    @allure.step("Запрос на выход из системы")
    def logout_user(token):
        return requests.post(urls.BASE_URL + urls.USER_ENDPOINTS['LOGOUT'], headers={'authorization': token})
