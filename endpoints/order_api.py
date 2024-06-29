import allure
import requests

import urls


class OrderApi:
    @staticmethod
    @allure.step("Запрос на создание заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.ORDER_ENDPOINTS['CREATE_ORDER'], json=body)

    @staticmethod
    @allure.step("Запрос на получение списка заказов")
    def get_orders(token):
        headers = {'authorization': token}

        return requests.get(urls.BASE_URL + urls.ORDER_ENDPOINTS['GET_ORDERS'], headers=headers)
