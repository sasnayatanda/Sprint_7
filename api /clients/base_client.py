import requests
from typing import Optional, Dict, Any
import allure


class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}
    
    @allure.title("Выполнение запроса GET")    
    def get(self, path: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        response = requests.get(
            f"{self.base_url}{path}", 
            params=params,
            headers=self.headers
        )
        return {
            'status_code': response.status_code,
            'body': response.json() if response.content else None,
            'text': response.text
        }
    
    @allure.title("Выполнение запроса POST")
    def post(self, path: str, json: Optional[Dict] = None) -> Dict[str, Any]:
        response = requests.post(
            f"{self.base_url}{path}",
            json=json,  # Используем json= вместо body=
            headers=self.headers
        )
        return {
            'status_code': response.status_code,
            'body': response.json() if response.content else None,
            'text': response.text
        }
    
    @allure.title("Выполнение запроса DELETE")    
    def delete(self, path: str) -> Dict[str, Any]:
        response = requests.delete(
            f"{self.base_url}{path}",
            headers=self.headers
        )
        return {
            'status_code': response.status_code,
            'body': response.json() if response.content else None,
            'text': response.text
        }