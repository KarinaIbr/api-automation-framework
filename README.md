# API Automation Framework

An API test automation framework built with Python, requests, and pytest.

The project focuses on clean client architecture, environment-based configuration, reusable request logic, and maintainable API test design.

## Key Features

- Clear separation of concerns
- Reusable BaseClient for shared request logic
- Dedicated AddressesClient for endpoint-specific actions
- Environment-based configuration via `.env`
- Centralized settings management
- Structured pytest-based test design
- Clean foundation for further CRUD, negative, and data-driven API scenarios

## Tech Stack

- Python
- requests
- pytest
- python-dotenv

## Project Structure

```text
api-automation-framework/
├── api/
│   ├── __init__.py
│   └── clients/
│       ├── __init__.py
│       ├── base_client.py
│       └── addresses_client.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── tests/
│   ├── __init__.py
│   └── api/
│       ├── __init__.py
│       └── test_addresses.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Current Coverage

### Addresses API
- Create address returns `200 OK`
- Response contains a non-empty `id`

## Configuration

The project uses environment variables for runtime configuration.

Expected variables in `.env`:

```env
API_BASE_URL=your_base_url
AUTH_SECRET=your_auth_secret
```

## How to Run

```bash
git clone https://github.com/karinaibr/api-automation-framework.git
cd api-automation-framework
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Run a Specific Test

```bash
pytest tests/api/test_addresses.py -k test_create_address_returns_200 -v
```

## Framework Notes

- `BaseClient` contains shared API request behavior such as base URL, headers, session, timeout, and reusable HTTP methods.
- `AddressesClient` extends the base layer with address-specific endpoint actions.
- Test logic is kept separate from client logic for better readability and maintainability.

## Next Steps

- Extend the create flow with `GET by id`
- Strengthen response assertions
- Introduce reusable payload strategy
- Add negative scenarios
- Expand toward broader CRUD coverage