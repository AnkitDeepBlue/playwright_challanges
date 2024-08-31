from playwright.sync_api import Page
from functools import cached_property

from locaters.locater_service import LocatorService
from utils.helpers import HelperBot
from proxy.sorting_proxy import SortingProxy
from utils.logger import setup_logger


class TablePage:
    def __init__(self, page: Page, locator_service: LocatorService):
        self.page = page
        self.locators = locator_service.lambda_table
        self.bot = HelperBot(page)
        self.sorting_proxy = SortingProxy(page)
        self.logger = setup_logger(self.__class__.__name__)

    def load(self):
        """Load the page by navigating to the URL."""
        self.logger.info("Loading the page")
        self.page.goto(self.locators.url)

    def sort_by_column(self, column_name: str, order: str):
        """Sort the table by the specified column and order."""
        self.logger.info(f"Sorting by column: {column_name} with order: {order}")
        ele = self.bot.process_selector(self.locators.name_column_header.format(column_name=column_name))
        return self.sorting_proxy.do_sorting(ele, order)

    @cached_property
    def table_contents(self):
        """Get the contents of the table."""
        self.logger.info("Getting table contents")
        return self.bot.get_elements(self.locators.table_rows)

    def search(self, name: str):
        """Search for the specified name in the table."""
        self.logger.info(f"Searching for name: {name}")
        self.page.fill(self.locators.search_input, name)
        self.page.press(self.locators.search_input, "Enter")

    def search_contains_text(self, text: str):
        """Check if the search results contain the specified text."""
        self.logger.info(f"Checking if search results contain text: {text}")
        rows = self.bot.get_elements(self.locators.row_locator.format(text=text))
        if any(text in row.inner_text() for row in rows):
            self.bot.take_screenshot(self.page, "search_contains_text")
            return True
        return False
