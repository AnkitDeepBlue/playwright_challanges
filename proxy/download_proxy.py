import os
from playwright.sync_api import Page
from utils.helpers import HelperBot
from utils.logger import setup_logger
from exceptions.custom_exceptions import DownloadFailedException, FileSaveException


class DownloadProxy:
    def __init__(self, page: Page):
        self.page = page
        self.logger = setup_logger(self.__class__.__name__)
        self.downloads = {}
        self.bot = HelperBot(self.page)

    def download_csv(self, download_button_locator: str, download_dir: str):
        self.logger.info("Clicking on the 'CSV' button to download the table data as CSV")
        try:
            with self.page.expect_download() as download_info:
                self.page.click(download_button_locator)
            download = download_info.value
        except Exception as e:
            raise DownloadFailedException(f"Failed to initiate the download: {str(e)}")

        try:
            download_path = self.bot.get_download_path(download_dir, download.suggested_filename)
            download.save_as(download_path)
        except Exception as e:
            raise FileSaveException(download_path, f"Failed to save the downloaded file: {str(e)}")

        self.downloads[download.suggested_filename] = download_path
        self.logger.info(f"CSV downloaded to {download_path}")
        return download_path

    def verify_csv_download(self, filename: str) -> bool:
        self.logger.info(f"Verifying if the CSV file {filename} is downloaded")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        return True
