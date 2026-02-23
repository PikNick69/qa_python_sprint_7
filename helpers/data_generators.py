import random
import string

class CourierDataGenerator:
    """Генерация данных для курьеров"""
    
    @staticmethod
    def generate_random_string(length):
        """Генерация случайной строки"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    @staticmethod
    def generate_courier_data():
        """Генерация данных для создания курьера"""
        login = CourierDataGenerator.generate_random_string(10)
        password = CourierDataGenerator.generate_random_string(10)
        first_name = CourierDataGenerator.generate_random_string(10)
        
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }


class OrderDataGenerator:
    """Генерация данных для заказов"""
    
    @staticmethod
    def generate_order_data(color=None):
        """Генерация данных для заказа с указанным цветом"""
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }
        
        if color is not None:
            if isinstance(color, list):
                order_data["color"] = color
            else:
                order_data["color"] = [color]
        
        return order_data