import time

from playwright.sync_api import Page
from functools import cached_property
from utils.helpers import MainPage
from utils.sorting_proxy import SortingProxy
from utils.logger import setup_logger

class TablePage:
    def __init__(self, page: Page):
        self.page = page
        self.main_page = MainPage(page)
        self.sorting_proxy = SortingProxy(page)
        self.logger = setup_logger(self.__class__.__name__)

    @cached_property
    def locators(self):
        return {
            "url": "https://www.lambdatest.com/selenium-playground/table-sort-search-demo",
            "name_column_header": "th:has-text('{column_name}')",
            "table_rows": "table tbody tr",
            "search_input": "input[type='search']"
        }

    def load(self):
        self.logger.info("Loading the page")
        self.page.goto(self.locators["url"])

    def sort_by_column(self, column_name: str, order):
        self.logger.info(f"Sorting by column: {column_name} with order: {order}")
        ele = self.main_page.get_elements(self.locators["name_column_header"].format(column_name=column_name))
        return self.sorting_proxy.do_sorting(ele[0], order)

    @cached_property
    def table_contents(self):
        self.logger.info("Getting table contents")
        return self.main_page.get_elements(self.locators["table_rows"])

    def search(self, name):
        self.logger.info(f"Searching for name: {name}")
        self.page.fill(self.locators["search_input"], name)
        self.page.press(self.locators["search_input"], "Enter")

    def search_contains_text(self, text: str):
        self.logger.info(f"Checking if search results contain text: {text}")
        row_locator = f"table tbody tr:has-text('{text}')"
        rows = self.main_page.get_elements(row_locator)
        if any(text in row.inner_text() for row in rows):
            MainPage.take_screenshot(self.page, "search_contains_text")
            return True
        return False