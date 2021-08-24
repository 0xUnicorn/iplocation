import requests
from dataclasses import dataclass


class Connector:

    URL = "http://ip-api.com/json/"

    x_ttl = 60
    x_rl = 45

    def connect_to_api(self, ip: str) -> dict:
        self._validate_counter()
        response = self._get_request(
            url=f"{self.URL}{ip}"
        )
        self._update_counters(response.headers)
        return response.json()

    def _get_request(self, url: str) -> requests.Response:
        return requests.get(
            url=url
        )

    def _update_counters(self, headers: dict) -> None:
        self.x_ttl = headers['X-Ttl']
        self.x_rl = headers['X-Rl']

    def _validate_counter(self) -> None:
        if self.x_rl == 0:
            raise NoAvailableRequests(f"No available requests left. Wait for {self.x_ttl} seconds, and try again.")


class NoAvailableRequests(Exception):

    pass
