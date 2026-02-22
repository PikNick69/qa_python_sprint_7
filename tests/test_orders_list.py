import allure
from helpers import OrderMethods

@allure.epic("Управление заказами")
@allure.feature("Список заказов")
class TestOrdersList:
    
    @allure.title("Получение списка заказов")
    @allure.description("Проверка структуры ответа при получении списка заказов")
    def test_get_orders_list_returns_list(self):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = OrderMethods.get_orders_list()
        
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200
        
        with allure.step("Проверить структуру ответа"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)