from dataclasses import dataclass


@dataclass(frozen=True)
class LambdaUpload:
    url: str = "https://www.lambdatest.com/selenium-playground/upload-file-demo"
    upload_file_field: str = "//input[@id='file']"
    message: str =  "//*[@id='error']"


