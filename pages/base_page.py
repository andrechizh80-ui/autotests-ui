from re import Pattern
from playwright.sync_api import Page, expect
import allure


class BasePage:
    """
    Базовый класс для работы со страницами
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url)

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload()

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
