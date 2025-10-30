"""Smoke tests for the sample application's home page."""
from __future__ import annotations

from playwright.sync_api import Page

from tests.pages.home_page import HomePage


def test_home_page_has_title(page: Page) -> None:
    """Verify that the home page title is displayed."""

    home_page = HomePage(page).load()
    title_text = home_page.get_title_text()

    assert title_text, "Expected the page title to be present"
