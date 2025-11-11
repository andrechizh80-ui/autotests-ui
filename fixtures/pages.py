from page_forms.registration_page import RegistrationPage
from page_forms.dashboard_page import DashboardPage
import pytest
from playwright.sync_api import Page

@pytest.fixture
def registration_page(chromium_page:Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)

@pytest.fixture
def dashboard_page(chromium_page:Page) -> DashboardPage:
    return DashboardPage(chromium_page)
