import pytest
from api.clients.addresses_client import AddressesClient
from data.address_payloads import build_address_payload


@pytest.fixture
def addresses_client():
    return AddressesClient()

@pytest.fixture
def created_address(addresses_client):

    payload = build_address_payload()
    response = addresses_client.create_address(payload)
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}. "
        f"Response body: {response.text}"
    )

    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"]
    created_id = response_data["id"]

    yield {"id": created_id, "payload": payload}

    delete_response = addresses_client.delete_address(created_id)
    assert delete_response.status_code in (200, 404), (
        f"Expected status code 200 or 404, got {delete_response.status_code}. "
        f"Response body: {delete_response.text}"
    )





