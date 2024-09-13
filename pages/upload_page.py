from locaters.locater_service import LocatorService
from utils.helpers import HelperBot
from utils.logger import setup_logger
from playwright.sync_api import Page




class UploadPage:
    def __init__(self, page:Page, locator_service: LocatorService):
        self.page = page
        self.locators = locator_service.lambda_upload
        self.bot = HelperBot(self.page)
        self.logger = setup_logger(self.__class__.__name__)

    def load(self):
        """Load the page by navigating to the URL."""
        self.logger.info("Loading the page")
        self.page.goto(self.locators.url)

    def upload_file(self, file_path: str):
        """ Upload file """
        self.logger.info(f"Uploading the file from {file_path}")
        self.bot.process_selector(self.locators.upload_file_field).set_input_files(f'{file_path}')

    def assert_message_after_upload(self, message):
        assert self.bot.process_selector(self.locators.message).text_content() == message
