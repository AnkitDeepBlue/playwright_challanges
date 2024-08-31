import pytest
from playwright.sync_api import sync_playwright

from locaters.locater_service import LocatorService
from pages.jansunwai import JanSunwai
from pages.download_page import DownloadPage
from pages.table_page import TablePage


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        yield context
        context.close()
        browser.close()


@pytest.fixture
def locator_service():
    """Provide the LocatorService for accessing page element locators."""
    return LocatorService()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def table_page(page, locator_service: LocatorService):
    yield TablePage(page, locator_service)


@pytest.fixture
def download_page(page, locator_service: LocatorService):
    yield DownloadPage(page, locator_service)


@pytest.fixture
def JanSunwai_page(page):
    yield JanSunwai(page)
