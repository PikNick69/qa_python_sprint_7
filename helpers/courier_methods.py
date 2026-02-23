import requests
from data.urls import ApiUrls

class CourierMethods:
    """Методы для работы с курьерами"""
    
    @staticmethod
    def create_courier(courier_data):
        """Создание курьера"""
        url = ApiUrls.get_full_url(ApiUrls.COURIER_CREATE)
        return requests.post(url, data=courier_data)
    
    @staticmethod
    def login_courier(login_data):
        """Авторизация курьера"""
        url = ApiUrls.get_full_url(ApiUrls.COURIER_LOGIN)
        return requests.post(url, data=login_data)
    
    @staticmethod
    def delete_courier(courier_id):
        """Удаление курьера"""
        if courier_id:
            url = ApiUrls.get_courier_delete_url(courier_id)
            return requests.delete(url)
    
    @staticmethod
    def get_courier_id(login, password):
        """Получение ID курьера по логину и паролю"""
        login_data = {"login": login, "password": password}
        response = CourierMethods.login_courier(login_data)
        if response.status_code == 200:
            return response.json().get("id")
        return None