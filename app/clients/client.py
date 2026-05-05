import requests
from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, base_url: str):
        self.url = base_url

    def _get(self, endpoint: str, params: dict = None):  # creates HTTP request logic for all child classes
        url = self.base_url + endpoint

        response = requests.get(url=url, params=params)
        response.raise_for_status()
        return response.json()
    
    @abstractmethod
    def get_teams(self):  # public method that allows child classes to indirectly acess the HTTP logic above
        pass


class ESPNClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_teams(self):
        return self._get("/teams")  # uses the private method implemented on the base class