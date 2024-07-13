import allure
from playwright.sync_api import Page
from playwright.sync_api import Locator


class MainPage:
    def __init__(self, page: Page):
        self.page = page


    def get_elements(self, selector):
        return self.page.query_selector_all(selector)

    @staticmethod
    def get_attribute(element: Locator, attribute):
        return element.get_attribute(attribute)

    @staticmethod
    def take_screenshot(page: Page, name: str):
        screenshot_path = f"screenshots/{name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)