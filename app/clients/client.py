import requests
from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _get(self, endpoint: str, params: dict = None):  # creates HTTP request logic for all child classes
        url = self.base_url + endpoint

        response = requests.get(url=url, params=params)
        response.raise_for_status()
        return response.json()
    
    @abstractmethod
    def get_teams(self, params: dict = None):  # public method that allows child classes to indirectly acess the HTTP logic above
        pass

    @abstractmethod
    def get_team_by_ref(self, team_url):
        pass


class ESPNClient(BaseClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_teams(self, params: dict = None):
        return self._get("/teams", params=params)  # uses the private method implemented on the base class
    
    def get_team_by_ref(self, team_url):
        return self._get(team_url)