from exceptions.custom_exceptions import SliderValueNotReachedException
from playwright.sync_api import Page, Locator
from utils.helpers import HelperBot


class SliderProxy:
    def __init__(self, page: Page):
        self.page = page
        self.bot = HelperBot(self.page)

    def move_slider_to_value(self, slider_element: Locator, slider_output_element: Locator, target_value: int):
        """
        Move the slider to the specified target value by comparing the slider output.
        """

        min_value = int(slider_element.get_attribute('min'))
        max_value = int(slider_element.get_attribute('max'))
        initial_value = int(slider_output_element.text_content())

        current_value = initial_value
        for attempt in range(3):
            slider_bounding_box = slider_element.bounding_box()
            if not slider_bounding_box:
                raise SliderValueNotReachedException("Slider element not found or has no bounding box.")

            slider_width = slider_bounding_box['width']
            y = slider_bounding_box['y'] + slider_bounding_box['height'] / 2
            start_x = slider_bounding_box['x']

            ratio = (target_value - min_value) / (max_value - min_value)
            current_x = start_x + ratio * slider_width

            self.page.mouse.move(start_x, y)
            self.page.mouse.down()
            try:
                self.page.mouse.move(current_x, y, steps=10)
                current_value = int(slider_output_element.text_content())
                if current_value == target_value:
                    return current_value
                if current_value == initial_value:
                    # Drag had no effect, likely a stale bounding box (e.g. late layout shift). Retry.
                    continue

                step = 1 if current_value < target_value else -1
                for _ in range(50):
                    if current_value == target_value:
                        return current_value
                    current_x += step
                    self.page.mouse.move(current_x, y)
                    current_value = int(slider_output_element.text_content())
            finally:
                self.page.mouse.up()

        raise SliderValueNotReachedException(f"Failed to move the slider to the target value: {target_value}. "
                                             f"Final value was: {current_value}")

    #I want one more method in SliderProxy class which will return the current value of the slider
