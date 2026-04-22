from data.address_payloads import build_address_payload
import allure


@allure.title("Address full lifecycle: create, update, and delete verification")
def test_address_full_lifecycle(addresses_client):
    # Create resource and verify baseline state
    initial_payload = build_address_payload()
    create_response = addresses_client.create_address(initial_payload)
    assert create_response.status_code == 200, (
        f"Expected status code 200, got {create_response.status_code}, "
        f"Response body: {create_response.text}"
    )

    created_response_data = create_response.json()
    assert "id" in created_response_data
    assert created_response_data["id"]

    created_id = created_response_data["id"]

    get_after_create_response = addresses_client.get_address_by_id(created_id)
    assert get_after_create_response.status_code == 200, (
        f"Expected status code 200, got {get_after_create_response.status_code}, "
        f"Response body: {get_after_create_response.text}"
    )

    get_after_create_data = get_after_create_response.json()
    assert "address" in get_after_create_data
    assert get_after_create_data["address"]

    # Baseline state
    baseline_address = get_after_create_data["address"]

    # Patch resource and verify updated state
    patch_payload = {
        "address": {
            "fullName": {
                "firstName": "NEW",
                "lastName": "INFO",
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
        f"Expected status code 200, got {patch_response.status_code}, "
        f"Response body: {patch_response.text}"
    )

    get_after_patch_response = addresses_client.get_address_by_id(created_id)
    assert get_after_patch_response.status_code == 200, (
        f"Expected status code 200, got {get_after_patch_response.status_code}, "
        f"Response body: {get_after_patch_response.text}"
    )

    get_after_patch_data = get_after_patch_response.json()
    assert "address" in get_after_patch_data
    assert get_after_patch_data["address"]

    updated_address = get_after_patch_data["address"]
    assert updated_address["fullName"]["firstName"] == patch_payload["address"]["fullName"]["firstName"]
    assert updated_address["fullName"]["lastName"] == patch_payload["address"]["fullName"]["lastName"]

    # Unchanged-field verification
    assert updated_address["company"] == baseline_address["company"]
    assert updated_address["addressLine1"] == baseline_address["addressLine1"]
    assert updated_address["addressLine2"] == baseline_address["addressLine2"]
    assert updated_address["city"] == baseline_address["city"]

    # Delete resource and verify it is no longer available
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