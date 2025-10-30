"""Page object for the CS sample application's landing page."""
from typing import Final

from playwright.sync_api import expect

from config.settings import BASE_URL
from tests.pages.base_page import BasePage


class HomePage(BasePage):
    """Encapsulate behaviour of the application's home page."""

    TITLE: Final[str] = "#cs-content h1"

    def load(self) -> "HomePage":
        """Navigate to the home page and wait for the title."""

        self.open(BASE_URL)
        expect(self.locator(self.TITLE)).to_be_visible()
        return self

    def get_title_text(self) -> str:
        """Return the page title text."""

        return self.locator(self.TITLE).inner_text().strip()
