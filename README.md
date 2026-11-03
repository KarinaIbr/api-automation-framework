# API Automation Framework

[**View Allure Report**](https://karinaibr.github.io/api-automation-framework/)

API test automation framework for an address management service, built with Python, requests, and pytest.

The project covers address creation, retrieval, updates, deletion, and negative API scenarios. Besides checking response status codes, the tests verify actual resource data through follow-up requests.

## Test Coverage

**API Operations**
- Create an address and verify the returned data
- Retrieve an address by ID and compare it with the original payload
- Update selected fields using `PATCH` and `fieldMask`
- Verify updated fields and confirm that unrelated fields remain unchanged
- Delete an address and check that subsequent requests return `404`

**Full Resource Lifecycle**

A separate test covers the entire flow using the same resource:

`POST → GET → PATCH → GET → DELETE → GET (404)`

**Negative Scenarios**
- Invalid, empty, and missing `fieldMask`
- Empty request bodies and missing or empty address objects
- Requests using non-existing resource IDs
- Error response messages and application error codes
- Resource state verification after rejected updates

## Framework Structure

- `api/clients/` contains `BaseClient` for HTTP requests and `AddressesClient` for endpoint-specific methods.
- `data/address_payloads.py` handles test data generation using Faker and predefined address fields.
- `config/settings.py` loads environment variables and request configuration.
- `conftest.py` manages pytest fixtures, resource cleanup, and Allure metadata.
- `tests/api/` separates operation tests, negative scenarios, and the full lifecycle test.

The `created_address` fixture handles setup and cleanup, so individual tests don't have to repeat that logic.

## Tech Stack

Python, requests, pytest, Faker, python-dotenv, Allure Report, GitHub Actions, GitHub Pages.

## Running Tests Locally

Clone the repository and install dependencies:

```bash
git clone https://github.com/KarinaIbr/api-automation-framework.git
cd api-automation-framework
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with the required configuration:

```env
API_BASE_URL=your_api_base_url
AUTH_SECRET=your_authorization_value
```

A valid authentication credential is required. The local `.env` file is excluded from Git.

Run the test suite:

```bash
pytest tests/api -v --alluredir=allure-results
```

Generate and open the Allure report (Allure CLI required):

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## CI & Reporting

GitHub Actions runs the API tests, generates an Allure report, and publishes it to GitHub Pages.

The workflow is triggered manually rather than on every push because the API requires a valid, short-lived authentication credential.

The workflow reads its configuration from GitHub Actions secrets.

[**View Published Allure Report**](https://karinaibr.github.io/api-automation-framework/)

## A Bug I Found

While testing `PATCH` requests, I noticed that combining a valid `fieldMask` path with an unknown one returned `500 Internal Server Error` instead of the expected `400 Bad Request`.

The address itself remained unchanged, but the API was treating invalid client input as a server error.

I kept the failing test in the suite using `pytest.mark.xfail(strict=True)` and documented the issue in [GitHub Issue #1](https://github.com/KarinaIbr/api-automation-framework/issues/1).

I also check the address state after rejected updates. An error response doesn't necessarily mean the data was left untouched.
