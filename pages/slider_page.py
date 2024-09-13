from locaters.locater_service import LocatorService
from utils.helpers import HelperBot
from utils.logger import setup_logger
from proxy.slider_proxy import SliderProxy
from playwright.sync_api import Page


class SliderPage:
    def __init__(self, page: Page, locator_service: LocatorService):
        self.page = page
        self.locators = locator_service.lambda_slider
        self.bot = HelperBot(self.page)
        self.logger = setup_logger(self.__class__.__name__)
        self.slider_proxy = SliderProxy(self.page)

    def load(self):
        """Load the page by navigating to the URL."""
        self.logger.info("Loading the page")
        self.page.goto(self.locators.url)

    def move_slider_to_value(self, target_value: int):
        """Move the slider to the specified target value by comparing the slider output."""
        self.logger.info(f"Moving the slider to the value: {target_value}")

        slider = self.bot.process_selector(self.locators.slider_bar)
        slider_output = self.bot.process_selector(self.locators.slider_output)

        final_value = self.slider_proxy.move_slider_to_value(slider, slider_output, target_value)

        self.logger.info(f"Slider moved to: {final_value}")
        return final_value

