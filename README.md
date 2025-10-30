# Test Automation Example

This repository showcases a Python UI automation skeleton built with
Playwright, pytest, and the Page Object Model.

## Project layout

```
├── .github/                # CI/CD settings
├── config/                 # Global settings (base URL, etc.)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image for running the test suite
└── tests/
    ├── conftest.py         # Shared fixtures
    ├── data/               # Test data samples
    ├── fixtures/           # Browser and Playwright fixtures
    ├── pages/              # Page Object Model abstractions
    └── test_home_page.py   # Example smoke test
```

## Getting started locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Running in Docker

You can build and execute the tests inside a container without installing
any system dependencies locally. The image is based on the official
Playwright runtime so the browsers are preinstalled.

```bash
docker build -t playwright-tests .
docker run --rm playwright-tests
```

The base image already ships with the Playwright browsers, so no extra
setup commands are required inside the container.

## Continuous integration

A GitHub Actions workflow (`.github/workflows/tests.yml`) runs the full pytest
suite on every push and pull request targeting the `main` branch. The workflow
uses the same Playwright container image, installs the Python dependencies with
`pip`, and executes the tests to keep the automation suite healthy.

## Running in Docker

You can build and execute the tests inside a container without installing
any system dependencies locally. The Dockerfile uses the
`mcr.microsoft.com/playwright/python:v1.44.0-jammy` base image so the
Playwright browsers are preinstalled.

```bash
docker build -t playwright-tests .
docker run --rm playwright-tests
```

The base image already ships with the Playwright browsers, so no extra
setup commands are required inside the container.

## Continuous integration

A GitHub Actions workflow (`.github/workflows/tests.yml`) runs the full pytest
suite on every push and pull request targeting the `main` branch. The workflow
uses the same Playwright container image, installs the Python dependencies with
`pip`, and executes the tests to keep the automation suite healthy.

## Next steps

- Expand configuration management if different environments are required.
- Integrate rich reporting (Allure, Playwright traces, CI test analytics).
- Expand the Page Objects and test coverage according to product requirements.
