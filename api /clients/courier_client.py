from typing import Dict, Any, Optional
from api.clients.base_client import BaseClient
import allure

class CourierClient(BaseClient):
    
    @allure.title("Создание курьера")
    def create_courier(self, login: str, password: str, first_name: str) -> Dict[str, Any]:
        """Создание курьера POST /api/v1/courier"""
        json_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return self.post("/api/v1/courier", json=json_data)
    
    @allure.title("Авторизация курьера")
    def login_courier(self, login: str, password: str) -> Dict[str, Any]:
        """Авторизация курьера POST /api/v1/courier/login"""
        json_data = {
            "login": login,
            "password": password
        }
        return self.post("/api/v1/courier/login", json=json_data)
    
    @allure.title("Удаление курьера")
    def delete_courier(self, courier_id: int) -> Dict[str, Any]:
        """Удаление курьера DELETE /api/v1/courier/{id}"""
        return self.delete(f"/api/v1/courier/{courier_id}")