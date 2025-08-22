import pytest
import random
import string
from api.client_factory import ClientFactory

@pytest.fixture
def courier_client():
    return ClientFactory.courier()

@pytest.fixture
def order_client():
    return ClientFactory.order()

def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@pytest.fixture
def random_courier_data():
    """Фикстура возвращает данные для создания курьера"""
    return {
        "login": f"test_{generate_random_string(8)}",
        "password": generate_random_string(10),
        "first_name": generate_random_string(8)
    }

@pytest.fixture
def registered_courier(courier_client, random_courier_data):
    """Фикстура создает курьера и возвращает его данные + ID, автоматически удаляет после теста"""
    # Регистрируем курьера
    response = courier_client.create_courier(
        random_courier_data["login"],
        random_courier_data["password"], 
        random_courier_data["first_name"]
    )
    
    # Если регистрация успешна - получаем ID
    courier_id = None
    if response['status_code'] == 201:
        login_response = courier_client.login_courier(
            random_courier_data["login"],
            random_courier_data["password"]
        )
        courier_id = login_response['body']['id']
    
    # Возвращаем словарь с данными (читаемо!)
    yield {
        "login": random_courier_data["login"],
        "password": random_courier_data["password"],
        "first_name": random_courier_data["first_name"],
        "id": courier_id
    }
    
    # Teardown - удаляем курьера после теста
    if courier_id:
        courier_client.delete_courier(courier_id)