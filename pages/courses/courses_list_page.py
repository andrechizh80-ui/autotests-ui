from playwright.sync_api import Page

from components.courses.course_view_component import CourseViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage
from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from elements.button import Button


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.courses_list_toolbar_view = CoursesListToolbarViewComponent(page)
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_view = CourseViewComponent(page)

        self.course_view_button = Button(page,'course-view-menu-button', 'Course view button')
        self.course_edit_button = Button(page,'course-view-edit-menu-item-text','Course edit button')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here '
        )

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        self.course_view.check_visible(index, title, max_score, min_score, estimated_time)

    def click_edit(self):
        self.course_view_button.click()
        self.course_edit_button.click()
