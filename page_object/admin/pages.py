from page_object.global_objects import *
from page_object.admin_operations.locators import AdminLoginPageLocator, AdminDashboardPageLocator, \
    AdminUserPageLocator, AdminAddUserPageLocator

admin_login_locator = AdminLoginPageLocator()
admin_dashboard_locator = AdminDashboardPageLocator()
admin_users_list_locator = AdminUserPageLocator()
admin_add_user_locator = AdminAddUserPageLocator()


class AdminLoginPage(BasePage):

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_page(self):
        self._web_driver.find_element(admin_login_locator.username_field)

    def login(self, username, password):
        if username != '' and password != '':
            self._web_driver.send_value(admin_login_locator.username_field, username)
            self._web_driver.send_value(admin_login_locator.password_field, password)
        self._web_driver.click_element(admin_login_locator.sign_in_button)

    def verify_login_fail(self):
        self._web_driver.verify_text(admin_login_locator.incorrect_login_message,
                                     'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')


class AdminDashboardPage(BasePage):
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_pass(self):
        self._web_driver.verify_text(admin_dashboard_locator.dashboard_title_text, 'Site administration')

    def logout(self):
        time.sleep(1)
        self._web_driver.click_element(admin_dashboard_locator.logout_link)
        self.verify_logout_page()

    def verify_logout_page(self):
        self._web_driver.verify_text(admin_dashboard_locator.logout_page_title, "Logged out")

    def goto_users_list(self):
        self._web_driver.scroll_to(admin_dashboard_locator.user_link)
        self._web_driver.click_element(admin_dashboard_locator.user_link)


class AdminUsersListPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_users_list_page(self):
        self._web_driver.verify_text(admin_users_list_locator.user_title_text, "Select user to change")
