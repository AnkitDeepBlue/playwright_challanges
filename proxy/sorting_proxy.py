from playwright.sync_api import Page, Locator
from utils.helpers import HelperBot
from exceptions.custom_exceptions import SortingFailedException
import time


class SortingProxy:
    def __init__(self, page: Page):
        self.page = page
        self.bot = HelperBot(page)
        self.my_sorting = {}

    def get_sorting_state(self, selector: str) -> str:
        """Retrieve the current sorting state of the element."""
        element = self.bot.process_selector(selector)
        return self.bot.get_attribute(element, 'class')

    def do_sorting(self, selector: str, expected_sorting: str, max_attempts: int = 5):
        """Perform sorting by clicking the element until the desired sorting state is achieved."""
        current_sorting = self.get_sorting_state(selector)

        try:
            attempts = 0
            while current_sorting != expected_sorting and attempts < max_attempts:
                element = self.bot.process_selector(selector)
                element.click()
                time.sleep(0.3)
                current_sorting = self.get_sorting_state(selector)
                attempts += 1

            if current_sorting != expected_sorting:
                raise SortingFailedException(
                    f"Failed to sort to {expected_sorting} after {attempts} attempts.")

            element = self.bot.process_selector(selector)
            self.my_sorting[element.text_content()] = current_sorting
            return self.my_sorting

        except Exception as e:
            raise SortingFailedException(f"An error occurred while sorting: {str(e)}")

    def get_current_sorting(self, selector: str):
        """Return the current sorting state of the element."""
        return self.get_sorting_state(selector)
