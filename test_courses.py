from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        page.get_by_test_id('registration-form-email-input').locator('input').fill('user.name@gmail.com')
        page.get_by_test_id('registration-form-username-input').locator('input').fill('username')
        page.get_by_test_id('registration-form-password-input').locator('input').fill('password')
        page.get_by_test_id('registration-page-registration-button').click()
        browser_context = context.storage_state()

        new_context = browser.new_context(storage_state=browser_context)
        page = new_context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        course_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_title).to_be_visible()
        expect(course_title).to_have_text('Courses')

        results_div = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(results_div).to_be_visible()
        expect(results_div).to_have_text('There is no results')

        empty_block = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_block).to_be_attached()
        expect(empty_block).to_be_enabled()

        result_text_block = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_text_block).to_have_text('Results from the load test pipeline will be displayed here')