import pytest
from playwright.sync_api import sync_playwright

from pages.jansunwai import JanSunwai
from pages.download_page import DownloadPage
from pages.table_page import TablePage
import certifi
import ssl

# Ensure SSL certificate verification using certifi's CA bundle
ssl_context = ssl.create_default_context(cafile=certifi.where())

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture
def table_page(page):
    yield TablePage(page)

@pytest.fixture
def download_page(page):
    yield DownloadPage(page)

@pytest.fixture
def JanSunwai_page(page):
    yield JanSunwai(page)