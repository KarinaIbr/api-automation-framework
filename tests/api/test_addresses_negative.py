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


@allure.title("Reject partial update with empty field mask")
def test_patch_address_with_empty_field_mask_is_rejected(addresses_client, created_address):
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

    empty_patch_payload = {
        "address": {
            "fullName": {
                "firstName": "Empty",
                "lastName": "Mask",
            },
        },
        "fieldMask": {
            "paths": []
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, empty_patch_payload)
    assert patch_response.status_code == 400,  (
        f"Expected status code == 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    error_data = patch_response.json()
    assert error_data["message"] == "field_mask must not be empty", (
        f"Expected error message 'field_mask must not be empty', "
        f"got {error_data['message']}. "
        f"Response body: {patch_response.text}"
    )

    assert error_data["details"]["applicationError"]["code"] == "missing_required_field", (
        f"Expected application error code 'missing_required_field', "
        f"got {error_data['details']['applicationError']['code']}. "
        f"Response body: {patch_response.text}"
    )

    after_empty_patch_response = addresses_client.get_address_by_id(created_id)
    assert after_empty_patch_response.status_code == 200, (
        f"Expected status code 200, got {after_empty_patch_response.status_code}. "
        f"Response body: {after_empty_patch_response.text}"
    )

    after_empty_patch_data = after_empty_patch_response.json()
    assert "address" in after_empty_patch_data
    assert after_empty_patch_data["address"]
    after_empty_patch_address = after_empty_patch_data["address"]

    assert after_empty_patch_address == baseline_address


@allure.title("Reject partial update with missing field mask")
def test_patch_address_with_missing_field_mask_is_rejected(addresses_client, created_address):
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

    missing_field_mask_payload = {
        "address": {
            "fullName": {
                "firstName": "Missing",
                "lastName": "FieldMask",
            },
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, missing_field_mask_payload)
    assert patch_response.status_code == 400,  (
        f"Expected status code == 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    error_data = patch_response.json()
    assert error_data["message"] == "field_mask must not be empty", (
        f"Expected error message 'field_mask must not be empty', "
        f"got {error_data['message']}. "
        f"Response body: {patch_response.text}"
    )

    assert error_data["details"]["applicationError"]["code"] == "missing_required_field", (
        f"Expected application error code 'missing_required_field', "
        f"got {error_data['details']['applicationError']['code']}. "
        f"Response body: {patch_response.text}"
    )

    after_missing_field_mask_response = addresses_client.get_address_by_id(created_id)
    assert after_missing_field_mask_response.status_code == 200, (
        f"Expected status code 200, got {after_missing_field_mask_response.status_code}. "
        f"Response body: {after_missing_field_mask_response.text}"
    )

    after_missing_field_mask_data = after_missing_field_mask_response.json()
    assert "address" in after_missing_field_mask_data
    assert after_missing_field_mask_data["address"]
    after_missing_field_mask_address = after_missing_field_mask_data["address"]

    assert after_missing_field_mask_address == baseline_address


@allure.title("Reject get address by non-existing id")
def test_get_address_by_non_existing_id_is_rejected(addresses_client):
    non_existing_id = "00000000-0000-0000-0000-000000000000"
    get_response = addresses_client.get_address_by_id(non_existing_id)
    assert get_response.status_code == 404, (
        f"Expected status code 404, got {get_response.status_code}. "
        f"Response body: {get_response.text}"
    )


@allure.title("Reject partial update for non-existing address id")
def test_patch_address_for_non_existing_id_is_rejected(addresses_client):
    non_existing_id = "99999999-9999-9999-9999-999999999999"
    patch_payload = {
        "address": {
            "fullName": {
                "firstName": "Karina",
                "lastName": "Ib",
            },
        },
        "fieldMask": {
            "paths": [
                "fullName.firstName",
                "fullName.lastName",
            ]
        },
    }

    patch_response = addresses_client.partial_update_address(non_existing_id, patch_payload)
    assert patch_response.status_code == 404, (
        f"Expected status code 404, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )


@allure.title("Return 404 when deleting non-existing address id")
def test_delete_address_for_non_existing_id_is_rejected(addresses_client):
    non_existing_id = "99999999-9999-9999-9999-999999999999"
    delete_response = addresses_client.delete_address(non_existing_id)

    assert delete_response.status_code == 404, (
        f"Expected status code 404, got {delete_response.status_code}. "
        f"Response body: {delete_response.text}"
    )


@allure.title("Reject partial update with empty request body")
def test_patch_address_with_empty_request_body_is_rejected(addresses_client, created_address):
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

    empty_payload = {}

    patch_response = addresses_client.partial_update_address(created_id, empty_payload)
    assert patch_response.status_code == 400, (
        f"Expected status code == 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    after_empty_payload_response = addresses_client.get_address_by_id(created_id)
    assert after_empty_payload_response.status_code == 200, (
        f"Expected status code 200, got {after_empty_payload_response.status_code}. "
        f"Response body: {after_empty_payload_response.text}"
    )

    after_empty_payload_data = after_empty_payload_response.json()
    assert "address" in after_empty_payload_data
    assert after_empty_payload_data["address"]
    after_empty_payload_address = after_empty_payload_data["address"]

    assert after_empty_payload_address == baseline_address


@allure.title("Reject partial update with missing address object")
def test_patch_address_with_missing_address_object_is_rejected(addresses_client, created_address):
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

    missing_address_payload = {
        "fieldMask": {
            "paths": [
                "fullName.firstName"
            ]
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, missing_address_payload)
    assert patch_response.status_code == 400, (
        f"Expected status code == 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    after_missing_address_response = addresses_client.get_address_by_id(created_id)
    assert after_missing_address_response.status_code == 200, (
        f"Expected status code 200, got {after_missing_address_response.status_code}. "
        f"Response body: {after_missing_address_response.text}"
    )

    after_missing_address_data = after_missing_address_response.json()
    assert "address" in after_missing_address_data
    assert after_missing_address_data["address"]
    after_missing_address_address = after_missing_address_data["address"]

    assert after_missing_address_address == baseline_address


@allure.title("Reject partial update with empty address object")
def test_patch_address_with_empty_address_object_is_rejected(addresses_client, created_address):
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

    empty_address_payload = {
        "address": {},
        "fieldMask": {
            "paths": [
                "fullName.firstName"
            ]
        },
    }

    patch_response = addresses_client.partial_update_address(created_id, empty_address_payload)
    assert patch_response.status_code == 400, (
        f"Expected status code == 400, got {patch_response.status_code}. "
        f"Response body: {patch_response.text}"
    )

    after_empty_address_response = addresses_client.get_address_by_id(created_id)
    assert after_empty_address_response.status_code == 200, (
        f"Expected status code 200, got {after_empty_address_response.status_code}. "
        f"Response body: {after_empty_address_response.text}"
    )

    after_empty_address_data = after_empty_address_response.json()
    assert "address" in after_empty_address_data
    assert after_empty_address_data["address"]
    after_empty_address_address = after_empty_address_data["address"]

    assert after_empty_address_address == baseline_address