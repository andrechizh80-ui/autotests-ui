import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page:CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(
            url='https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.check_visible_image_preview_empty_view()
        create_course_page.create_course_form.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.check_visible_image_preview_empty_view()

        create_course_page.upload_preview_image(file='./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill_form(
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
