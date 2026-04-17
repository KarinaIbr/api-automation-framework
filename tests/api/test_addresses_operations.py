import conftest
from api.clients.addresses_client import AddressesClient
from data.address_payloads import build_address_payload


def test_create_address_and_get_by_id(addresses_client):

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

    # Retrieve the created address by id
    get_response = addresses_client.get_address_by_id(created_id)
    assert get_response.status_code == 200, (
        f"Expected status code 200, got {get_response.status_code}, "
        f"Response body: {get_response.text}"
    )

    get_response_data = get_response.json()

    # Verify key fields in the returned address
    assert "address" in get_response_data

    returned_address = get_response_data["address"]

    assert returned_address["addressLine1"] == payload["address"]["addressLine1"]
    assert returned_address["city"] == payload["address"]["city"]
    assert returned_address["zipCode"] == payload["address"]["zipCode"]
    assert returned_address["company"] == payload["address"]["company"]
    assert get_response_data["isDefaultAddress"] == payload["setAsDefault"]
    assert returned_address["fullName"]["firstName"] == payload["address"]["fullName"]["firstName"]
    assert returned_address["fullName"]["lastName"] == payload["address"]["fullName"]["lastName"]
    assert returned_address["country"] == payload["address"]["country"]
    assert returned_address["subdivision"] == payload["address"]["subdivision"]

    delete_response = addresses_client.delete_address(created_id)
    assert delete_response.status_code == 200, (
        f"Expected status code 200, got {delete_response.status_code}. "
        f"Response body: {delete_response.text}"
    )


def test_patch_address_updates_name_fields(addresses_client, created_address):

    created_id = created_address["id"]
    payload = created_address["payload"]

    patch_payload = {
        "address": {
            "fullName": {
                "firstName": "Lady",
                "lastName": "Bug",
            },
        },
        "fieldMask": {
            "paths": [
                "fullName.firstName",
                "fullName.lastName",
            ]
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, patch_payload)
    assert patch_response.status_code == 200, (
        f"Expected status code 200, got {patch_response.status_code},"
        f"Response body: {patch_response.text}"
    )

    get_response = addresses_client.get_address_by_id(created_id)
    assert get_response.status_code == 200, (
        f"Expected status code 200, got {get_response.status_code},"
        f"Response body: {get_response.text}"
    )

    get_response_data = get_response.json()
    assert "address" in get_response_data
    assert get_response_data["address"]

    returned_address = get_response_data["address"]
    assert returned_address["fullName"]["firstName"] == patch_payload["address"]["fullName"]["firstName"]
    assert returned_address["fullName"]["lastName"] == patch_payload["address"]["fullName"]["lastName"]

    # Unchanged-field verification
    assert returned_address["company"] == payload["address"]["company"]


def test_delete_address_and_verify_it_is_not_found(addresses_client, created_address):

    created_id = created_address["id"]
    delete_response = addresses_client.delete_address(created_id)
    assert delete_response.status_code == 200, (
        f"Expected status code 200, got {delete_response.status_code}, "
        f"Response body: {delete_response.text}"
    )

    get_after_delete_response = addresses_client.get_address_by_id(created_id)
    assert get_after_delete_response.status_code == 404, (
        f"Expected status code 404, got {get_after_delete_response.status_code}, "
        f"Response body: {get_after_delete_response.text}"
    )


#     PUT for exemple

#     def test_put_address_updates_full_payload_fields(addresses_client):
#     payload = build_address_payload()
#     update_payload = copy.deepcopy(payload)
#
#     update_payload["address"]["company"] = "Lady Bug Studio"
#     update_payload["address"]["fullName"]["firstName"] = "Karina"
#     update_payload["address"]["fullName"]["lastName"] = "Smith"
#
#     response = addresses_client.create_address(payload)
#     assert response.status_code == 200, (
#         f"Expected status code 200, got {response.status_code}, "
#         f"Response body: {response.text}"
#     )
#
#     response_data = response.json()
#     assert "id" in response_data
#     assert response_data["id"]
#     created_id = response_data["id"]
#
#     put_response = addresses_client.update_address(created_id, update_payload)
#     assert put_response.status_code == 200, (
#         f"Expected status code 200, got {put_response.status_code}, "
#         f"Response body: {put_response.text}"
#     )
#
#     get_response = addresses_client.get_address_by_id(created_id)
#     assert get_response.status_code == 200, (
#         f"Expected status code 200, got {get_response.status_code},"
#         f"Response body: {get_response.text}"
#     )
#
#     get_response_data = get_response.json()
#     assert "address" in get_response_data
#     assert get_response_data["address"]
#
#     returned_address = get_response_data["address"]
#     assert returned_address["fullName"]["firstName"] == update_payload["address"]["fullName"]["firstName"]
#     assert returned_address["fullName"]["lastName"] == update_payload["address"]["fullName"]["lastName"]
#     assert returned_address["company"] == update_payload["address"]["company"]
#
#     assert returned_address["zipCode"] == payload["address"]["zipCode"]
