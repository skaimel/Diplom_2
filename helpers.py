import allure

import data
from endpoints.user_api import UserApi


@allure.step("Регистрация пользователя и получение тела запроса для авторизации")
def get_login_user_data(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_password = body.get('password')
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Регистрация пользователя и получение тела запроса с невалидным email для авторизации")
def get_login_request_with_invalid_email(body):
    UserApi.register_user(body)
    auth_email = data.fake.email()
    auth_password = body.get('password')
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Регистрация пользователя и получение тела запроса с невалидным password для авторизации")
def get_login_request_with_invalid_password(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_password = data.fake.password()
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Регистрация пользователя и получение тела запроса без email для авторизации")
def get_login_request_without_email(body):
    UserApi.register_user(body)
    auth_password = body.get('password')
    auth_body = {'password': auth_password}
    return auth_body


@allure.step("Регистрация пользователя и получение тела запроса без password для авторизации")
def get_login_request_without_password(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_body = {'email': auth_email}
    return auth_body