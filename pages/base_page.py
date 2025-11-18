from re import Pattern
from playwright.sync_api import Page, expect
import allure
from tools.logger import get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    """
    Базовый класс для работы со страницами
    """

    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening the url "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url)

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload()

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
