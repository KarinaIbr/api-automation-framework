from api.clients.base_client import BaseClient


class AddressesClient(BaseClient):
    ENDPOINT = "addresses"

    def create_address(self, payload):
        return self.post(self.ENDPOINT, payload)

    def get_address_by_id(self,address_id):
        endpoint = f"{self.ENDPOINT}/{address_id}"
        return self.get(endpoint)

    def get_all_addresses(self):
        return self.get(self.ENDPOINT)
