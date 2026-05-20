import allure


@allure.title("Reject partial update with invalid field mask")
def test_patch_address_with_invalid_field_mask_is_rejected(addresses_client, created_address):
    created_id = created_address["id"]
    baseline_response = addresses_client.get_address_by_id(created_id)

    assert baseline_response.status_code == 200, (
        f"Expected status code 200, got {baseline_response.status_code}. "
        f"Response body: {baseline_response.text}"
    )

    baseline_data = baseline_response.json()
    assert "address" in baseline_data
    assert baseline_data["address"]
    baseline_address = baseline_data["address"]

    invalid_patch_payload = {
        "address": {
            "fullName": {
                "firstName": "NEW",
                "lastName": "INFO",
            },
        },
        "fieldMask": {
            "paths": [
                "fullName.middleName"
            ]
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, invalid_patch_payload)
    assert patch_response.status_code >= 400,  (
        f"Expected status code >= 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    after_invalid_patch_response = addresses_client.get_address_by_id(created_id)
    assert after_invalid_patch_response.status_code == 200, (
        f"Expected status code 200, got {after_invalid_patch_response.status_code}. "
        f"Response body: {after_invalid_patch_response.text}"
    )

    after_invalid_patch_data = after_invalid_patch_response.json()
    assert "address" in after_invalid_patch_data
    assert after_invalid_patch_data["address"]
    after_invalid_patch_address = after_invalid_patch_data["address"]

    assert after_invalid_patch_address == baseline_address


@allure.title("Reject get address by non-existing id")
def test_get_address_by_non_existing_id_is_rejected(addresses_client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    get_response = addresses_client.get_address_by_id(non_existing_id)
    assert get_response.status_code == 404, (
        f"Expected status code 404, got {get_response.status_code}. "
        f"Response body: {get_response.text}"
    )
