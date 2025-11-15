from re import Pattern
from playwright.sync_api import Page, expect


class BasePage:
    """
    Базовый класс для работы со страницами
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def reload(self):
        self.page.reload()

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
