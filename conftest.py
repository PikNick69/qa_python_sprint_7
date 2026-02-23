import pytest
from helpers import CourierDataGenerator, CourierMethods

@pytest.fixture
def courier_data_with_cleanup():
    """
    Фикстура для генерации данных курьера и очистки после теста
    """
    # Подготовка данных
    courier_data = CourierDataGenerator.generate_courier_data()
    
    # Передаем данные в тест
    yield courier_data
    
    # Teardown: удаление курьера после теста
    courier_id = CourierMethods.get_courier_id(
        courier_data["login"], 
        courier_data["password"]
    )
    if courier_id:
        CourierMethods.delete_courier(courier_id)

@pytest.fixture
def existing_courier(courier_data_with_cleanup):
    """
    Фикстура для создания существующего курьера
    """
    response = CourierMethods.create_courier(courier_data_with_cleanup)
    
    if response.status_code == 201:
        return courier_data_with_cleanup
    return None