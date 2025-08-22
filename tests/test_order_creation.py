import pytest
import allure


class TestOrderCreation:
    """Тесты для создания заказа POST /api/v1/orders"""
    
    @allure.title("CR_ORDER_1, CR_ORDER_2, CR_ORDER_3, CR_ORDER_4, CR_ORDER_5: Создание заказа с разными цветами")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"], 
        ["BLACK", "GREY"],
        [],
        None
    ], ids=["black_color", "grey_color", "both_colors", "empty_array", "no_color"])
    def test_create_order_with_different_colors(self, order_client, color):
        order_data = {
            "first_name": "Naruto",
            "last_name": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metro_station": 4,
            "phone": "+7 800 355 35 35",
            "rent_time": 5,
            "delivery_date": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        
        # Убираем None из color, если нужно
        if color is None:
            order_data.pop("color")
        
        response = order_client.create_order(**order_data)
        assert response['status_code'] == 201
        assert "track" in response['body']
        assert isinstance(response['body']['track'], int)

    @allure.title("CR_ORDER_6: Ошибка при отсутствии обязательного поля firstName")
    def test_create_order_missing_first_name(self, order_client):
        order_data = {
            "first_name": "",
            "last_name": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metro_station": 4,
            "phone": "+7 800 355 35 35",
            "rent_time": 5,
            "delivery_date": "2024-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }
        
        response = order_client.create_order(**order_data)
        # Этот тест может падать, согласно вашему чек-листу
        assert response['status_code'] == 400