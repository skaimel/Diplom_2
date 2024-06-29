import allure

import data
import helpers
from endpoints.order_api import OrderApi
from endpoints.user_api import UserApi


class TestOrders:
    @allure.title('Успешное получение списка заказов авторизованного пользователя')
    @allure.description('Получение списка заказов под авторизованным пользователем. Проверка статуса и тело ответа')
    def test_get_orders_authorized_user_success(self, get_default_user):
        login_body = helpers.get_login_user_data(get_default_user)
        UserApi.register_user(login_body)
        response_login_user = UserApi.login_user(login_body)
        token = response_login_user.json()['accessToken']
        response_get_orders = OrderApi.get_orders(token)

        assert (
            response_get_orders.status_code == data.HTTP_OK
            and response_get_orders.json()['success'] is True
            and response_get_orders.json()['orders'] is not None
        )

    @allure.title('Невозможность получения списка заказов неавторизованного пользователя')
    @allure.description('Получение списка заказов под неавторизованным пользователем. Проверка статуса и тело ответа')
    def test_get_orders_unauthorized_user_unauthorized(self):
        token = ""
        response_get_orders = OrderApi.get_orders(token)

        assert (
            response_get_orders.status_code == data.HTTP_UNAUTHORIZED
            and response_get_orders.json()['success'] is False
            and response_get_orders.json()['message'] == data.UNAUTHORIZED_ERROR
        )