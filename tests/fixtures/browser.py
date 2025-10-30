"""Playwright fixtures and session management."""
from __future__ import annotations

from typing import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from config.settings import BASE_URL


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Provide a shared Playwright instance for the test session."""

    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Launch a Chromium browser for the test session."""

    browser_instance: Browser = playwright_instance.chromium.launch()
    yield browser_instance
    browser_instance.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Create an isolated browser context for each test."""

    browser_context: BrowserContext = browser.new_context(base_url=BASE_URL)
    yield browser_context
    browser_context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Yield a fresh page for the current test."""

    page_instance: Page = context.new_page()
    yield page_instance
    page_instance.close()
