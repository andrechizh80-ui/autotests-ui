import pytest
from page_forms.registration_page import RegistrationPage
from page_forms.dashboard_page import DashboardPage
class TestRegistration:
    """
    Класс для тестов страницы регистрации
    """

    @pytest.mark.courses
    @pytest.mark.regression
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page:DashboardPage):
        registration_page.visit(
            url=' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form(email='user@mail.com',
                                                 username='username',
                                                 password='password')
        dashboard_page.check_title_visible()
