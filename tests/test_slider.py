import pytest
import allure


@pytest.mark.slider_test
@allure.feature('Slider Test')
@allure.description("Testing move slider bar as per given value")
def test_slider(slider_page):
    with allure.step("Load slider page"):
        slider_page.load()

    with allure.step("Moving slider"):
        slider_page.move_slider_to_value(55)


