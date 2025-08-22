import pytest
import allure

class TestOrderList:
    """Тесты для получения списка заказов GET /api/v1/orders"""
    
    @allure.title("LIST_0F_ORDER_1: Получение непустого списка заказов")
    def test_get_orders_list(self, order_client):
        """LIST_0F_ORDER_1: Получение непустого списка заказов"""
        response = order_client.get_orders_list()
        assert response['status_code'] == 200
        assert "orders" in response['body']
        assert isinstance(response['body']['orders'], list)

    