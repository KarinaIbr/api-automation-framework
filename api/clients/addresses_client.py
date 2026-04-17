from api.clients.base_client import BaseClient


class AddressesClient(BaseClient):
    ENDPOINT = "addresses"

    def get_all_addresses(self):
        return self.get(self.ENDPOINT)

    def get_address_by_id(self, address_id):
        endpoint = f"{self.ENDPOINT}/{address_id}"
        return self.get(endpoint)

    def create_address(self, payload):
        return self.post(self.ENDPOINT, payload)

    def partial_update_address(self, address_id, payload):
        endpoint = f"{self.ENDPOINT}/{address_id}"
        return self.patch(endpoint, payload)

    def update_address(self, address_id, payload):
        endpoint = f"{self.ENDPOINT}/{address_id}"
        return self.put(endpoint, payload)

    def delete_address(self, address_id):
        endpoint = f"{self.ENDPOINT}/{address_id}"
        return self.delete(endpoint)
