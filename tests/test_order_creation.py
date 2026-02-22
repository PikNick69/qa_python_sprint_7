import allure
import pytest
from helpers import OrderDataGenerator, OrderMethods

@allure.epic("Управление заказами")
@allure.feature("Создание заказа")
class TestOrderCreation:
    
    @allure.title("Создание заказа с различными цветами")
    @allure.description("Параметризованный тест создания заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [],
        None
    ])
    def test_create_order_with_different_colors(self, color):
        with allure.step(f"Создать заказ с цветом {color}"):
            order_data = OrderDataGenerator.generate_order_data(color)
            response = OrderMethods.create_order(order_data)
        
        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 201
            assert "track" in response.json()
            assert isinstance(response.json()["track"], int)