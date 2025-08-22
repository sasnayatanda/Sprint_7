import pytest
import allure


class TestCourierLogin:
    """Тесты для авторизации курьера POST /api/v1/courier/login"""
    
    @allure.title("LOG_COUR_1: Успешная авторизация курьера")
    def test_login_courier_success(self, courier_client, registered_courier):
        response = courier_client.login_courier(
            registered_courier["login"],
            registered_courier["password"]
        )
        assert response['status_code'] == 200
        assert "id" in response['body']

    @allure.title("LOG_COUR_2: Ошибка при неправильном пароле")
    def test_login_wrong_password(self, courier_client, registered_courier):
        response = courier_client.login_courier(
            registered_courier["login"],
            "wrong_password"
        )
        assert response['status_code'] == 404
        assert "Учетная запись не найдена" in response['body']['message']

    @allure.title("LOG_COUR_3: Ошибка при неправильном логине")
    def test_login_wrong_login(self, courier_client, registered_courier):
        response = courier_client.login_courier(
            "wrong_login",
            registered_courier["password"]
        )
        assert response['status_code'] == 404
        assert "Учетная запись не найдена" in response['body']['message']

    @allure.title("LOG_COUR_4, LOG_COUR_5: Отсутствие полей для авторизации")
    @pytest.mark.parametrize("test_data", [
        {"login": "", "password": "124312"},
        {"login": "test_login", "password": ""}
    ], ids=["missing_login", "missing_password"])
    def test_login_missing_fields(self, courier_client, test_data):
        response = courier_client.login_courier(
            test_data["login"],
            test_data["password"]
        )
        assert response['status_code'] == 400
        assert "Недостаточно данных" in response['body']['message']

    @allure.title("LOG_COUR_6: Авторизация несуществующего пользователя")
    def test_login_nonexistent_user(self, courier_client):
        response = courier_client.login_courier("nonexistent", "password")
        assert response['status_code'] == 404
        assert "Учетная запись не найдена" in response['body']['message']