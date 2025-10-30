"""Page object for the CS sample application's landing page."""

from playwright.sync_api import Locator, Page, expect

from utils.utils import form_page_url_by_language
from utils.dataclasses import PageLanguage


class HomePage():
    """Encapsulate behaviour of the application's home page."""

    def __init__(self, page: Page, language: str = PageLanguage.CZ.value):
        self.page: Page = page
        self.page_url: str = form_page_url_by_language(language=language)

        # locators
        self.contact_us_button: Locator = page.locator("[id=\"_desktop_contact_link\"]")
        self.search_field: Locator = page.locator("[id=\"search_widget\"]")
        self.choose_language_button: Locator = page.locator("[id=\"_desktop_language_selector\"]")
        self.main_logo: Locator = page.locator("[id=\"_desktop_logo\"]")


    def open(self):
        """Navigate to the home page and check the main logo is there."""

        self.page.goto(self.page_url)
        expect(self.main_logo).to_be_visible()
