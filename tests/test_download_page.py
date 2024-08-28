import pytest
import allure
import os


@pytest.mark.download_test
@allure.feature('Table Data Download')
@allure.story('Download table data as CSV')
@allure.description("Download the csv file")
def test_download_table_as_csv(download_page):
    download_page.load()
    os.path.join(os.getcwd(), "downloads")
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    with allure.step("Downloading the table data as CSV"):
        download_path = download_page.download_csv(download_dir)

    with allure.step("Verifying the CSV download"):
        is_downloaded = download_page.verify_csv_download(download_path)
        assert is_downloaded, "The CSV file was not downloaded correctly."
