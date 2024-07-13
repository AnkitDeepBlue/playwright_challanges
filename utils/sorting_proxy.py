from playwright.sync_api import Page, Locator
from utils.helpers import MainPage

class SortingProxy:
    def __init__(self, page: Page):
        self.page = page
        self.my_sorting = {}
        self.current_sorting = {}

    @staticmethod
    def get_sorting_state(element: Locator) -> str:
        return MainPage.get_attribute(element, 'class')

    def do_sorting(self, element: Locator, expected_sorting: str):
        current_sorting = self.get_sorting_state(element)
        while current_sorting != expected_sorting:
            element.click()
            current_sorting = self.get_sorting_state(element)
        self.my_sorting[element.text_content()] = current_sorting
        return self.my_sorting


    def get_current_sorting(self, element: Locator):
        return self.get_sorting_state(element)


