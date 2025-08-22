import pytest
import random
import string
import allure

class TestCourierCreation:
    """Тесты для создания курьера POST /api/v1/courier"""
    
    @allure.title("id CR_COUR_1")
    def test_create_courier_success(self, courier_client, random_courier_data):
        """CR_COUR_1: Успешное создание курьера с обязательными полями"""
        response = courier_client.create_courier(
            random_courier_data["login"],
            random_courier_data["password"],
            random_courier_data["first_name"]
        )
        assert response['status_code'] == 201
        assert response['body']['ok'] is True
    @allure.title("id CR_COUR_2")
    def test_create_duplicate_courier(self, courier_client, registered_courier):
        """CR_COUR_2: Нельзя создать двух одинаковых курьеров"""
        response = courier_client.create_courier(
            registered_courier["login"],
            registered_courier["password"],
            registered_courier["first_name"]
        )
        assert response['status_code'] == 409
        assert "уже используется" in response['body']['message']

    @pytest.mark.parametrize("missing_field, test_data", [
        ("login", {"login": "", "password": "124312", "first_name": "test"}),
        ("password", {"login": "test_login", "password": "", "first_name": "test"})
    ], ids=["missing_login", "missing_password"])
    @allure.title("id CR_COUR_3, CR_COUR_4")
    def test_create_courier_missing_required_fields(self, courier_client, missing_field, test_data):
        """CR_COUR_3, CR_COUR_4: Отсутствие обязательных полей login и password"""
        response = courier_client.create_courier(
            test_data["login"],
            test_data["password"],
            test_data["first_name"]
        )
        assert response['status_code'] == 400
        assert "Недостаточно данных" in response['body']['message']

    @allure.title("id CR_COUR_5")
    def test_create_courier_missing_first_name_duplicate_login(self, courier_client, registered_courier):
        """
        CR_COUR_5: Ошибка при отсутствии поля firstName (не обязательное поле)
        с логином, который уже существует
        """
        # Пытаемся создать курьера с существующим логином, но без firstName
        response = courier_client.create_courier(
            registered_courier["login"],  # Используем существующий логин
            "new_password_123",           # Новый пароль
            ""                            # Пустое firstName
        )
        
        # Должна быть ошибка 409, а не 400
        assert response['status_code'] == 409, f"Ожидался статус 409, но получили {response['status_code']}"
        assert "уже используется" in response['body']['message'], \
            f"В сообщении об ошибке нет ожидаемого текста. Получено: {response['body']['message']}"

    @allure.title("id CR_COUR_6")
    def test_create_courier_empty_body(self, courier_client):
        """CR_COUR_6: Пустое тело запроса"""
        response = courier_client.create_courier("", "", "")
        assert response['status_code'] == 400