from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    expect(page.get_by_test_id('registration-page-registration-button')).to_be_disabled()

    page.get_by_test_id('registration-form-email-input').locator('input').type('user.name@gmail.com')
    page.get_by_test_id('registration-form-username-input').locator('input').type('username')
    page.get_by_test_id('registration-form-password-input').locator('input').type('password')

    expect(page.get_by_test_id('registration-page-registration-button')).not_to_be_disabled()
