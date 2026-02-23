import requests
from data.urls import ApiUrls

class OrderMethods:
    """Методы для работы с заказами"""
    
    @staticmethod
    def create_order(order_data):
        """Создание заказа"""
        url = ApiUrls.get_full_url(ApiUrls.ORDER_CREATE)
        return requests.post(url, json=order_data)
    
    @staticmethod
    def get_orders_list():
        """Получение списка заказов"""
        url = ApiUrls.get_full_url(ApiUrls.ORDERS_LIST)
        return requests.get(url)