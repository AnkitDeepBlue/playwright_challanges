import os
import allure
from playwright.sync_api import Page, Locator
from exceptions.custom_exceptions import LocatorNotFoundException


class HelperBot:
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

    def process_selector(self, selector, timeout=5000, wait_state="visible"):
        try:
            element = self.page.wait_for_selector(selector, timeout=timeout, state=wait_state)
            return element
        except TimeoutError as e:
            raise LocatorNotFoundException(f"Failed to locate element: {selector}") from e

    @staticmethod
    def get_download_path(download_dir: str, filename: str) -> str:
        """Construct and return the full path for the download directory and file name."""
        if not os.path.isabs(download_dir):
            project_root = HelperBot.get_current_project_root()
            download_dir = os.path.join(project_root, download_dir)

        os.makedirs(download_dir, exist_ok=True)
        return os.path.join(download_dir, filename)

    @staticmethod
    def get_current_project_root():
        """Return the current project root directory."""
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_download_directory(self):
        """Return the default download directory path."""
        return self.get_download_path("downloads", "")

