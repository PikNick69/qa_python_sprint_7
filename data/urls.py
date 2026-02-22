class ApiUrls:
    """Класс для хранения всех URL эндпоинтов API"""
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    # Courier endpoints
    COURIER_CREATE = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    COURIER_DELETE = "/api/v1/courier/{courier_id}"
    
    # Order endpoints
    ORDER_CREATE = "/api/v1/orders"
    ORDERS_LIST = "/api/v1/orders"
    
    @classmethod
    def get_full_url(cls, endpoint):
        """Получить полный URL для эндпоинта"""
        return f"{cls.BASE_URL}{endpoint}"
    
    @classmethod
    def get_courier_delete_url(cls, courier_id):
        """Получить URL для удаления курьера с подставленным ID"""
        return f"{cls.BASE_URL}{cls.COURIER_DELETE.format(courier_id=courier_id)}"