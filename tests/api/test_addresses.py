import pytest
from api.clients.addresses_client import AddressesClient


@pytest.fixture
def addresses_client():
    return AddressesClient()

def test_create_address_returns_200(addresses_client):
    payload = {
        "address": {
            "fullName": {
                "firstName": "Anna",
                "lastName": "Miller",
            },
            "company": "Miller Studio",
            "taxInfo": {
                "id": None,
                "type": None,
            },
            "addressLine1": "4537 Monte Mar Drive",
            "addressLine2": "45",
            "street": {
                "name": None,
                "number": None,
            },
            "city": "El Dorado Hills",
            "country": "USA",
            "subdivision": "CA",
            "zipCode": "95762",
            "phoneNumber": None,
            "location": {
                "latitude": 38.6382313,
                "longitude": -121.0728334,
            },
        },
        "setAsDefault": False,
    }

    response = addresses_client.create_address(payload)
    assert response.status_code == 200, (f"Expected status code 200, got {response.status_code}. "
                                         f"Response body: {response.text}")

    response_data = response.json()

    # Verify that the created address returned a non-empty id
    assert "id" in response_data
    assert response_data["id"]
