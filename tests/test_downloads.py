import pytest
import allure


@pytest.mark.download_test
@allure.feature('Table Data Download')
@allure.story('Download table data as CSV')
@allure.description("Download the csv file and verify its presence")
def test_download_table_as_csv(download_page):
    with allure.step("Loading the download page"):
        download_page.load()

    download_dir = download_page.bot.get_download_directory()

    with allure.step("Downloading the table data as CSV"):
        download_path = download_page.download_csv(download_dir)

    with allure.step("Verifying the CSV download"):
        is_downloaded = download_page.verify_csv_download(download_path)
        assert is_downloaded, "The CSV file was not downloaded correctly."

    with allure.step("Attaching the CSV file to the Allure report"):
        allure.attach.file(download_path, name="Downloaded CSV", attachment_type=allure.attachment_type.CSV)