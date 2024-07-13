from functools import cached_property
from playwright.sync_api import Page
from utils.download_proxy import DownloadProxy
from utils.logger import setup_logger


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)
        self.download_proxy = DownloadProxy(page)

    @cached_property
    def locators(self):
        return {
            "url": "https://www.lambdatest.com/selenium-playground/table-data-download-demo",
            "csv_button": "//span[normalize-space()='CSV']"
        }

    def load(self):
        self.logger.info("Loading the download page")
        self.page.goto(self.locators["url"])

    def download_csv(self, download_dir: str):
        return self.download_proxy.download_csv(self.locators["csv_button"], download_dir)

    def verify_csv_download(self, filename: str) -> bool:
        return self.download_proxy.verify_csv_download(filename)