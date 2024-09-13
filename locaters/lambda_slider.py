from dataclasses import dataclass


@dataclass(frozen=True)
class LambdaSlider:
    url: str = "https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo"
    slider_bar: str = "//*[@class='sp__range sp__range-success']//input"
    slider_output: str = "//*[@class='sp__range sp__range-success']//output"

