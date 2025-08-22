from api.clients.courier_client import CourierClient
from api.clients.order_client import OrderClient

class ClientFactory:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    @classmethod
    def courier(cls) -> CourierClient:
        return CourierClient(cls.BASE_URL)
    
    @classmethod
    def order(cls) -> OrderClient:
        return OrderClient(cls.BASE_URL)