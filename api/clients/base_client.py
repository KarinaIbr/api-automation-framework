import requests
from config.settings import API_BASE_URL, AUTH_SECRET, TIMEOUT


class BaseClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.auth_secret = AUTH_SECRET
        self.timeout = TIMEOUT
        self.headers = {"Authorization": self.auth_secret}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, timeout=self.timeout)
        return response

    def post(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=payload, timeout=self.timeout)
        return response

    def put(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, json=payload, timeout=self.timeout)
        return response

    def patch(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.patch(url, json=payload, timeout=self.timeout)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, timeout=self.timeout)
        return response
