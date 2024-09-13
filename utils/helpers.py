import os
from pathlib import Path

import allure
from playwright.sync_api import Page, Locator
from exceptions.custom_exceptions import LocatorNotFoundException


class HelperBot:
    def __init__(self, page: Page):
        self.page = page
        self.upload_dir = self.get_or_create_directory('uploads')

    def get_elements(self, selector):
        return self.page.query_selector_all(selector)

    @staticmethod
    def get_attribute(element: Locator, attribute):
        return element.get_attribute(attribute)

    def take_screenshot(self, name: str, attach_to_allure: bool = False):
        screenshot_path = f"screenshots/{name}.png"
        self.page.screenshot(path=screenshot_path)

        if attach_to_allure:
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

    @staticmethod
    def find_project_root() -> Path:
        """Find the project root by searching for the 'requirements.txt' file."""
        current_dir = Path(__file__).resolve().parent

        while current_dir != current_dir.root:
            if (current_dir/'requirements.txt').exists():
                return current_dir
            current_dir = current_dir.parent

        raise FileNotFoundError("Project root with 'requirements.txt' not found.")

    @staticmethod
    def get_or_create_directory(dir_name: str) -> str:
        """Create a directory relative to the project root if it doesn't exist and return the directory path."""
        project_root = HelperBot.find_project_root()
        dir_path = project_root/dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        return str(dir_path)


    def get_upload_directory(self):
        return self.upload_dir
