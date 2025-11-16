import allure
import pytest

from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(
            url=AppRoute.COURSES_CREATE)

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.create_course_form.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.check_visible_image_preview_empty_view()

        create_course_page.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Blini",
            estimated_time="10 min",
            description="Blini so sgushenkoy",
            max_score="1000",
            min_score="100"
        )

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.courses_list_toolbar_view.check_visible()
        courses_list_page.check_visible_course_card(
            index=0,
            title="Blini",
            estimated_time="10 min",
            max_score="1000",
            min_score="100"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(
            url=AppRoute.COURSES_CREATE)

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.create_course_form.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.check_visible_image_preview_empty_view()

        create_course_page.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Blini",
            estimated_time="10 min",
            description="Blini so sgushenkoy",
            max_score="1000",
            min_score="100"
        )

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.courses_list_toolbar_view.check_visible()
        courses_list_page.check_visible_course_card(
            index=0,
            title="Blini",
            estimated_time="10 min",
            max_score="1000",
            min_score="100"
        )
        courses_list_page.click_edit()
        create_course_page.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="new_Blini",
            estimated_time="20 min",
            description="new Blini so sgushenkoy",
            max_score="2000",
            min_score="200"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.courses_list_toolbar_view.check_visible()
        courses_list_page.check_visible_course_card(
            index=0,
            title="new_Blini",
            estimated_time="20 min",
            max_score="2000",
            min_score="200"
        )
