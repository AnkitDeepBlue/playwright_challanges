import os
from playwright.sync_api import Page, Locator
from utils.logger import setup_logger

class DownloadProxy:
    def __init__(self, page: Page):
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)
        self.downloads = {}

    def download_csv(self, download_button_locator: str, download_dir: str):
        self.logger.info("Clicking on the 'CSV' button to download the table data as CSV")
        with self.page.expect_download() as download_info:
            self.page.click(download_button_locator)
        download = download_info.value
        download_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(download_path)
        self.downloads[download.suggested_filename] = download_path
        self.logger.info(f"CSV downloaded to {download_path}")
        return download_path

    def verify_csv_download(self, filename: str) -> bool:
        self.logger.info(f"Verifying if the CSV file {filename} is downloaded")
        return os.path.exists(filename)