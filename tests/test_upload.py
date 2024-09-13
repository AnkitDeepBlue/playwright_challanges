import pytest
import allure


@pytest.mark.upload_test
@allure.feature('Table Data Upload')
@allure.description("Upload pdf file and verify the message")
def test_upload_file(upload_page):
    with allure.step("Loading the uploads page"):
        upload_page.load()

    with allure.step("Downloading the table data as CSV"):
        upload_page.upload_file(f"{upload_page.bot.get_upload_directory()}/sample_text.pdf")

    with allure.step("Verifying the successful upload message appears"):
        upload_page.assert_message_after_upload("File Successfully Uploaded")
        upload_page.bot.take_screenshot(name="upload_confirmation", attach_to_allure=True)



