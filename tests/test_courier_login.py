import allure
import pytest
from helpers import CourierMethods
from data import ErrorMessages

@allure.epic("Управление курьерами")
@allure.feature("Авторизация курьера")
class TestCourierLogin:
    
    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка авторизации с валидными данными")
    def test_courier_login_success(self, existing_courier):
        with allure.step("Подготовить данные для авторизации"):
            login_data = {
                "login": existing_courier["login"],
                "password": existing_courier["password"]
            }
        
        with allure.step("Выполнить авторизацию"):
            response = CourierMethods.login_courier(login_data)
        
        with allure.step("Проверить успешную авторизацию"):
            assert response.status_code == 200
            assert "id" in response.json()
            assert isinstance(response.json()["id"], int)

    @allure.title("Авторизация с отсутствующим полем")
    @allure.description("Проверка, что нельзя авторизоваться без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field_fails(self, existing_courier, missing_field):
        with allure.step(f"Попытаться авторизоваться без поля {missing_field}"):
            login_data = {
                "login": existing_courier["login"],
                "password": existing_courier["password"]
            }
            login_data.pop(missing_field)
            
            response = CourierMethods.login_courier(login_data)
        
        with allure.step("Проверить, что получили ошибку"):
            assert response.status_code == 400
            assert response.json()["message"] == ErrorMessages.MISSING_LOGIN_DATA

    @allure.title("Авторизация с неверным логином")
    @allure.description("Проверка ошибки при вводе неверного логина")
    def test_courier_login_wrong_login_fails(self, existing_courier):
        with allure.step("Попытаться авторизоваться с неверным логином"):
            login_data = {
                "login": "wrong_login_123",
                "password": existing_courier["password"]
            }
            response = CourierMethods.login_courier(login_data)
        
        with allure.step("Проверить, что получили ошибку"):
            assert response.status_code == 404
            assert response.json()["message"] == ErrorMessages.INVALID_LOGIN

    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверка ошибки при вводе неверного пароля")
    def test_courier_login_wrong_password_fails(self, existing_courier):
        with allure.step("Попытаться авторизоваться с неверным паролем"):
            login_data = {
                "login": existing_courier["login"],
                "password": "wrong_password_123"
            }
            response = CourierMethods.login_courier(login_data)
        
        with allure.step("Проверить, что получили ошибку"):
            assert response.status_code == 404
            assert response.json()["message"] == ErrorMessages.INVALID_LOGIN

    @allure.title("Авторизация несуществующего пользователя")
    @allure.description("Проверка ошибки при авторизации несуществующего курьера")
    def test_courier_login_nonexistent_fails(self):
        with allure.step("Попытаться авторизоваться несуществующим курьером"):
            login_data = {
                "login": "nonexistent_login_123",
                "password": "nonexistent_pass_123"
            }
            response = CourierMethods.login_courier(login_data)
        
        with allure.step("Проверить, что получили ошибку"):
            assert response.status_code == 404
            assert response.json()["message"] == ErrorMessages.INVALID_LOGIN