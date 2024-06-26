import allure

import data
import helpers
from endpoints.order_api import OrderApi
from endpoints.user_api import UserApi


class TestCreateOrder:
    @allure.title('Успешный заказ авторизованного пользователя')
    @allure.description('Создание заказа под авторизованным пользователем.'
                        'Проверка статуса и тело ответа')
    def test_create_order_authorized_user_success(self, get_default_user):
        body = helpers.get_login_user_data(get_default_user)
        UserApi.login_user(body)
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_BODY)

        assert response_create_order.status_code == 200
        assert response_create_order.json()['success'] is True
        assert response_create_order.json()['name'] == data.CREATE_ORDER_NAME

    @allure.title('Невозможность заказа авторизованного пользователя с неверным хешем ингредиентов')
    @allure.description('Создание заказа с неверным хешем ингредиентов под авторизованным пользователем.'
                        'Проверка статуса и тело ответа')
    def test_create_order_with_invalid_ingredients_internal_server_error(self, get_default_user):
        body = helpers.get_login_user_data(get_default_user)
        UserApi.login_user(body)
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_WITH_INVALID_INGREDIENTS_BODY)

        assert (
            response_create_order.status_code == 500
            and data.INTERNAL_SERVER_ERROR in response_create_order.text
        )

    @allure.title('Невозможность заказа авторизованного пользователя без ингредиентов')
    @allure.description('Создание заказа без ингредиентов под авторизованным пользователем.'
                        'Проверка статуса и тело ответа')
    def test_create_order_without_ingredients_bad_request(self, get_default_user):
        body = helpers.get_login_user_data(get_default_user)
        UserApi.login_user(body)
        ingredients = {}
        response_create_order = OrderApi.create_order(ingredients)

        assert (
            response_create_order.status_code == 400
            and response_create_order.json()['success'] is False
            and response_create_order.json()['message'] == 'Ingredient ids must be provided'
        )

    @allure.title('Успешный заказ пользователя без авторизации')
    @allure.description('Создание заказа под неавторизованным пользователем.'
                        'Проверка статуса и тело ответа')
    def test_create_order_unauthorized_user_success(self):
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_BODY)

        assert (
            response_create_order.status_code == 200
            and response_create_order.json()['success'] is True
            and response_create_order.json()['name'] == data.CREATE_ORDER_NAME
        )