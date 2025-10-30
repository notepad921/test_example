"""Global fixtures for the test suite."""
from __future__ import annotations

from tests.fixtures import browser as browser_fixtures


# Re-export fixtures so they are discoverable by pytest.
browser = browser_fixtures.browser
page = browser_fixtures.page
context = browser_fixtures.context
