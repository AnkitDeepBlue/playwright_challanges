from exceptions.custom_exceptions import SliderValueNotReachedException
from playwright.sync_api import Page, ElementHandle
from utils.helpers import HelperBot


class SliderProxy:
    def __init__(self, page: Page):
        self.page = page
        self.bot = HelperBot(self.page)

    def move_slider_to_value(self, slider_element: ElementHandle, slider_output_element: ElementHandle, target_value: int):
        """
        Move the slider to the specified target value by comparing the slider output.
        """

        slider_bounding_box = slider_element.bounding_box()
        if not slider_bounding_box:
            raise SliderValueNotReachedException("Slider element not found or has no bounding box.")

        slider_width = slider_bounding_box['width']

        for i in range(-slider_width // 2, slider_width * 2, 4):
            x_offset = slider_bounding_box['x'] + i
            self.page.mouse.move(x_offset, slider_bounding_box['y'] + slider_bounding_box['height'] / 2)
            self.page.mouse.down()

            current_value = int(slider_output_element.text_content())

            if current_value == target_value:
                return current_value

        raise SliderValueNotReachedException(f"Failed to move the slider to the target value: {target_value}. "
                                             f"Final value was: {current_value}")

    #I want one more method in SliderProxy class which will return the current value of the slider
