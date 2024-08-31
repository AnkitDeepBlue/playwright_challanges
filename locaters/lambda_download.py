from dataclasses import dataclass


@dataclass(frozen=True)
class LambdaDownload:
    url: str = "https://www.lambdatest.com/selenium-playground/table-data-download-demo"
    csv_button: str = "//span[normalize-space()='CSV']"

