from playwright.sync_api import Page, expect
import allure
from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    @allure.step("Check visible view component {title}")
    def check_visible(self, title):
        expect(self.title).to_have_text(title)