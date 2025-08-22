from typing import Dict, Any, Optional, List
from api.clients.base_client import BaseClient
import allure

class OrderClient(BaseClient):
    
    @allure.title("Создание заказа")
    def create_order(
        self,
        first_name: str,
        last_name: str,
        address: str,
        metro_station: int,
        phone: str,
        rent_time: int,
        delivery_date: str,
        comment: str,
        color: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Создание заказа POST /api/v1/orders"""
        json_data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color or []  # Если color None, используем пустой список
        }
        return self.post("/api/v1/orders", json=json_data)
    
    @allure.title("Получение списка заказов")
    def get_orders_list(self, limit: Optional[int] = None, page: Optional[int] = None) -> Dict[str, Any]:
        """Получение списка заказов GET /api/v1/orders"""
        params = {}
        if limit:
            params["limit"] = limit
        if page:
            params["page"] = page
            
        return self.get("/api/v1/orders", params=params)