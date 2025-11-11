from page_forms.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    """
    Красс для работы со страницей Dashboard
    """
    def __init__(self, page: Page):
        super().__init__(page)

        # локаторы для блока Dashboard
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

        # методы для работы с формами/элементами на странице
    def check_title_visible(self):
        expect(self.dashboard_title).to_be_visible(), 'Тайтл DashBoard не найден на странице'

