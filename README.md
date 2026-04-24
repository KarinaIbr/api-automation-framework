# API Automation Framework

## Live Allure Report

[Open API Allure Report](https://karinaibr.github.io/api-automation-framework/)

An API test automation framework built with Python, requests, and pytest.

The framework validates real API behavior through operation-focused tests and a full resource lifecycle scenario:
create → get → patch → verify persistence → delete → verify deletion.

It includes structured API clients, environment-based configuration, dynamic test data generation with Faker, cleanup through pytest fixtures, and Allure reporting published via GitHub Pages.

## Key Features

- Clear separation of concerns between configuration, API clients, test data, fixtures, and tests
- Reusable `BaseClient` for shared request logic and HTTP methods
- Dedicated `AddressesClient` for endpoint-specific actions
- Environment-based configuration for base URL and authentication secret
- Dynamic address payload generation with Faker
- Pytest fixture with `yield` for resource setup and cleanup
- Operation-focused API tests for create, patch, and delete behavior
- Full resource lifecycle test: create → get → patch → verify persistence → delete → verify deletion
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
│       └── test_addresses_lifecycle.py
├── conftest.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Current Coverage

### Addresses API

The test suite currently covers:

- Create address and verify the response contains a non-empty `id`
- Get address by id and verify persisted address fields
- Partially update address data with `PATCH` and `fieldMask`
- Verify updated fields after a follow-up `GET` request
- Verify unchanged fields remain stable after partial update
- Delete address by id
- Verify deleted address is no longer available and returns `404`
- Full resource lifecycle scenario: create → get → patch → verify persistence → delete → verify deletion

## Configuration

The project uses environment variables for runtime configuration.

Expected variables in `.env`:

```env
API_BASE_URL=your_base_url
AUTH_SECRET=your_auth_secret
```

## How to Run Locally

```bash
git clone https://github.com/karinaibr/api-automation-framework.git
cd api-automation-framework
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

To generate Allure results locally:

```bash
pytest --alluredir=allure-results
```

To generate and open the Allure report:

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

## Framework Notes

- `BaseClient` contains shared API request behavior such as base URL, headers, session, timeout, and reusable HTTP methods.
- `AddressesClient` extends the base layer with address-specific endpoint actions.
- `address_payloads.py` keeps test data construction separate from test logic.
- The `created_address` fixture creates a resource before a test and cleans it up after the test with `yield`.
- Tests verify persisted behavior with follow-up `GET` requests instead of relying only on response status codes.
- Allure titles make the report readable for quick review.

## Reporting

The project includes Allure reporting for local and published test results.

The latest published report is available here:

[Open API Allure Report](https://karinaibr.github.io/api-automation-framework/)

The report is published through GitHub Pages using a manual GitHub Actions workflow.

## Notes About Authentication

This project uses an authentication secret provided through environment variables.

The secret is not stored in the repository. For local runs, it should be placed in `.env`. For GitHub Actions report publication, it should be stored as a GitHub Actions secret.

Because the current authentication token is temporary and updated manually, this project uses a manual report publication workflow instead of a standard CI run on every push.

## Next Steps

- Add negative API scenarios
- Add clearer validation for missing environment variables
- Consider removing unused endpoint methods that are not supported by the real API contract
- Continue improving README and project presentation for portfolio review