"""Smoke tests for the sample application's home page."""

import pytest
from playwright.sync_api import Page, Browser, BrowserContext

from tests.pages.home_page import HomePage
from utils.dataclasses import PageLanguage

@pytest.mark.parametrize(
        "language, expected_contact_us_button_text",
        [(PageLanguage.CZ.value, "Kontaktujte nás"), (PageLanguage.EN.value, "Contact us")]
    )
def test_home_page_has_2_languages(
        browser: Browser,
        language: str,
        expected_contact_us_button_text: str,
) -> None:
    """Verify the page has 2 language options and its changing change page content. """

    # prepare
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()

    # execute
    home_page: HomePage = HomePage(page, language=language)
    home_page.open()

    # check
    contact_us_button_text: str = home_page.contact_us_button.inner_text()
    assert contact_us_button_text == expected_contact_us_button_text,\
        (f"Contact us button text has wrong language: expected {expected_contact_us_button_text}, "
         f"real {contact_us_button_text}")


def test_home_page_has_expected_title(
        browser: Browser,
) -> None:
    """ Verify that the home page title is displayed. """

    # prepare
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    expected_title: str = "PrestaShop"

    # execute
    home_page: HomePage = HomePage(page, language=PageLanguage.CZ.value)
    home_page.open()
    title_text: str = home_page.page.title()

    # check
    assert title_text == expected_title, "Home page title is not equal to expected"
