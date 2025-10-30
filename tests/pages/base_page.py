"""Base page object definition."""
from playwright.sync_api import Locator, Page


class BasePage:
    """Common functionality shared across page objects."""

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def locator(self, selector: str) -> Locator:
        """Return a Locator for the given selector."""

        return self.page.locator(selector)
