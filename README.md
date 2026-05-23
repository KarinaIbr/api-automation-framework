# API Automation Framework

## Live Allure Report

[Open API Allure Report](https://karinaibr.github.io/api-automation-framework/)

An API test automation framework built with Python, requests, and pytest.

It focuses on real API behavior, reusable client structure, dynamic test data, reliable cleanup, negative scenario coverage, and clear Allure reporting.

## Key Features

- Clear separation between configuration, API clients, test data, fixtures, and tests
- Reusable `BaseClient` for shared request logic and HTTP methods
- Dedicated `AddressesClient` for address-specific API actions
- Environment-based configuration for base URL and authentication secret
- Sensitive runtime values kept outside the public repository
- Dynamic address payload generation with Faker
- Pytest fixture with `yield` for resource setup and cleanup
- Operation-focused tests for create, patch, and delete behavior
- Full resource lifecycle test covering create, get, patch, verify persistence, delete, and verify deletion
- Negative API scenarios for invalid field masks and non-existing address resources
- Allure reporting with readable test titles
- Published GitHub Pages report for quick review

## Tech Stack

- Python
- requests
- pytest
- python-dotenv
- Faker
- Allure Report
- GitHub Actions
- GitHub Pages

## Project Structure

```text
api-automation-framework/
├── .github/
│   └── workflows/
│       └── pages.yml
├── api/
│   ├── __init__.py
│   └── clients/
│       ├── __init__.py
│       ├── base_client.py
│       └── addresses_client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   ├── __init__.py
│   └── address_payloads.py
├── tests/
│   ├── __init__.py
│   └── api/
│       ├── __init__.py
│       ├── test_addresses_operations.py
│       ├── test_addresses_lifecycle.py
│       └── test_addresses_negative.py
├── conftest.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Current Coverage

### Addresses API

The test suite currently covers:

- Creating an address and verifying the response contains a non-empty `id`
- Getting an address by id and verifying persisted address fields
- Partially updating address data with `PATCH` and `fieldMask`
- Verifying updated fields after a follow-up `GET` request
- Verifying unchanged fields after a partial update
- Deleting an address by id
- Verifying a deleted address is no longer available and returns `404`
- Full resource lifecycle flow: create, get, patch, verify persistence, delete, and verify deletion
- Rejecting partial updates with an invalid `fieldMask`
- Verifying that an invalid partial update does not change the existing address state
- Returning `404` for getting an address by a non-existing id
- Returning `404` for patching an address by a non-existing id
- Returning `404` for deleting an address by a non-existing id

## Configuration

The framework uses environment-based runtime configuration.

Expected local variables:

```env
API_BASE_URL=your_base_url
AUTH_SECRET=your_auth_secret
```

Sensitive runtime values are kept outside the repository.

## Review Notes

The repository keeps source code public while sensitive runtime configuration remains private.

The published Allure Report provides current execution results for portfolio review.

## Local Execution

```bash
git clone https://github.com/karinaibr/api-automation-framework.git
cd api-automation-framework
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Generate Allure results locally:

```bash
pytest --alluredir=allure-results
```

Generate and open the Allure report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Run Specific Tests

Run operation-focused address tests:

```bash
pytest tests/api/test_addresses_operations.py -v
```

Run the full lifecycle test:

```bash
pytest tests/api/test_addresses_lifecycle.py -v
```

Run negative address tests:

```bash
pytest tests/api/test_addresses_negative.py -v
```

## Framework Notes

- `BaseClient` contains shared request behavior such as base URL, headers, session, timeout, and reusable HTTP methods.
- `AddressesClient` keeps address-specific endpoint actions separate from test logic.
- `address_payloads.py` keeps test data construction outside the test files.
- The `created_address` fixture creates a resource before a test and cleans it up after the test with `yield`.
- Tests verify persisted API behavior with follow-up `GET` requests, not only response status codes.
- Negative tests cover invalid contract behavior and non-existing resource handling.
- Allure titles make the report easier to read and review.

## Reporting

The project includes Allure reporting for local and published test results.

The latest published report is available here:

[Open API Allure Report](https://karinaibr.github.io/api-automation-framework/)

The report is published through GitHub Pages using a GitHub Actions workflow.
