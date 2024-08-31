from playwright.sync_api import Page, Locator
from utils.helpers import HelperBot
from exceptions.custom_exceptions import SortingFailedException


class SortingProxy:
    def __init__(self, page: Page):
        self.page = page
        self.bot = HelperBot(page)
        self.my_sorting = {}

    def get_sorting_state(self, element: Locator) -> str:
        """Retrieve the current sorting state of the element."""
        return self.bot.get_attribute(element, 'class')

    def do_sorting(self, element: Locator, expected_sorting: str, max_attempts: int = 5):
        """Perform sorting by clicking the element until the desired sorting state is achieved."""
        current_sorting = self.get_sorting_state(element)

        try:
            attempts = 0
            while current_sorting != expected_sorting and attempts < max_attempts:
                element.click()
                current_sorting = self.get_sorting_state(element)
                attempts += 1

            if current_sorting != expected_sorting:
                raise SortingFailedException(
                    f"Failed to sort {element.text_content()} to {expected_sorting} after {attempts} attempts.")

            self.my_sorting[element.text_content()] = current_sorting
            return self.my_sorting

        except Exception as e:
            raise SortingFailedException(f"An error occurred while sorting: {str(e)}")

    def get_current_sorting(self, element: Locator):
        """Return the current sorting state of the element."""
        return self.get_sorting_state(element)
