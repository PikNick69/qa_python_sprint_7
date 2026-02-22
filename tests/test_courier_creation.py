import allure
import pytest
from helpers import CourierDataGenerator, CourierMethods
from data import ErrorMessages

@allure.epic("Управление курьерами")
@allure.feature("Создание курьера")
class TestCourierCreation:
    
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка создания нового курьера с валидными данными")
    def test_create_courier_success(self, courier_data_with_cleanup):
        with allure.step("Отправить запрос на создание курьера"):
            response = CourierMethods.create_courier(courier_data_with_cleanup)
        
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

    @allure.title("Невозможно создать двух одинаковых курьеров")
    @allure.description("Проверка, что система не позволяет создать курьера с существующим логином")
    def test_create_duplicate_courier_fails(self, existing_courier):
        with allure.step("Создать первого курьера через фикстуру"):
            assert existing_courier, "Первый курьер не создан"
        
        with allure.step("Попытаться создать курьера с таким же логином"):
            duplicate_payload = {
                "login": existing_courier["login"],
                "password": "newpass123",
                "firstName": "NewName"
            }
            response = CourierMethods.create_courier(duplicate_payload)
        
        with allure.step("Проверить, что получили ошибку о существующем логине"):
            assert response.status_code == 409
            assert response.json()["message"] == ErrorMessages.COURIER_EXISTS

    @allure.title("Создание курьера с отсутствующим полем")
    @allure.description("Проверка, что нельзя создать курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_fails(self, missing_field):
        with allure.step(f"Создать данные курьера без поля {missing_field}"):
            courier_data = CourierDataGenerator.generate_courier_data()
            courier_data.pop(missing_field)
            
            response = CourierMethods.create_courier(courier_data)
        
        with allure.step("Проверить, что получили ошибку"):
            assert response.status_code == 400
            assert response.json()["message"] == ErrorMessages.MISSING_FIELD