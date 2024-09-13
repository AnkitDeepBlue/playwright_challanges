import pytest
import allure


@pytest.mark.slider_test
@allure.feature('Slider Test')
@allure.description("Testing move slider bar as per given value")
@pytest.mark.parametrize('slide_to', [50, 75, 100])
def test_slider(slider_page, slide_to):
    with allure.step("Load slider page"):
        slider_page.load()

    with allure.step("Moving slider"):
        slider_page.move_slider_to_value(slide_to)


