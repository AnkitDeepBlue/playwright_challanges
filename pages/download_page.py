from playwright.sync_api import Page
from locaters.locater_service import LocatorService
from proxy.download_proxy import DownloadProxy
from utils.logger import setup_logger
from utils.helpers import HelperBot


class DownloadPage:
    def __init__(self, page: Page, locator_service: LocatorService):
        self.page = page
        self.locators = locator_service.lambda_download
        self.logger = setup_logger(self.__class__.__name__)
        self.bot = HelperBot(page)
        self.download_proxy = DownloadProxy(page)

    def load(self):
        """Load the download page."""
        self.logger.info("Loading the download page")
        self.page.goto(self.locators.url)

    def download_csv(self, download_dir: str):
        """Download a CSV file to the specified directory."""
        return self.download_proxy.download_csv(self.locators.csv_button, download_dir)

    def verify_csv_download(self, filename: str) -> bool:
        """Verify if the CSV file was downloaded successfully."""
        return self.download_proxy.verify_csv_download(filename)

