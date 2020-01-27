from page_object.global_objects import *
from page_object.admin.locators import AdminLoginPageLocator, AdminDashboardPageLocator, \
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

    def goto_add_user_page(self):
        self._web_driver.scroll_to(admin_users_list_locator.user_add_button)
        self._web_driver.click_element(admin_users_list_locator.user_add_button)

    def verify_user_change_success(self, username):
        self._web_driver.verify_text(admin_users_list_locator.user_change_success,
                                     "The user " + username + " was changed successfully.")


class AdminAddUserPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_user_page(self):
        self._web_driver.verify_text(admin_add_user_locator.add_user_title_text, "Add user")

    def verify_change_user_page(self):
        self._web_driver.verify_text(admin_add_user_locator.add_user_change_user_title_text, "Change user")

    def select_group(self, groups):
        for group in groups:
            self._web_driver.send_value(admin_add_user_locator.add_user_group_search_text, group)
            if self._web_driver.verify_text(admin_add_user_locator.add_user_group_option, group):
                self._web_driver.click_element(admin_add_user_locator.add_user_group_option)
                self._web_driver.click_element(admin_add_user_locator.add_user_group_add_arrow_button)

    def select_permission(self, permissions):
        for permission in permissions:
            self._web_driver.send_value(admin_add_user_locator.add_user_permission_search_text, permission)
            if self._web_driver.verify_text(admin_add_user_locator.add_user_permission_option, permission):
                self._web_driver.click_element(admin_add_user_locator.add_user_permission_option)
                self._web_driver.click_element(admin_add_user_locator.add_user_permission_add_arrow_button)

    def create_user(self, username, password):
        self._web_driver.send_value(admin_add_user_locator.add_user_username_field, username)
        self._web_driver.send_value(admin_add_user_locator.add_user_password1_field, password)
        self._web_driver.send_value(admin_add_user_locator.add_user_password2_field, password)
        self._web_driver.click_element(admin_add_user_locator.add_user_save_button)
        self.verify_change_user_page()

    def change_user(self, first_name, last_name, email, is_active, is_staff, is_super_user, groups, permissions):
        self._web_driver.send_value(admin_add_user_locator.add_user_first_name_field, first_name)
        self._web_driver.send_value(admin_add_user_locator.add_user_last_name_field, last_name)
        self._web_driver.send_value(admin_add_user_locator.add_user_email_field, email)
        is_checked = self._web_driver.find_element(admin_add_user_locator.add_user_active_check).is_selected()
        if not is_checked & is_active:
            self._web_driver.click_element(admin_add_user_locator.add_user_active_check)
        is_checked = self._web_driver.find_element(admin_add_user_locator.add_user_super_user_check).is_selected()
        if not is_checked & is_super_user:
            self._web_driver.click_element(admin_add_user_locator.add_user_super_user_check)

        is_checked = self._web_driver.find_element(admin_add_user_locator.add_user_staff_check).is_selected()
        if not is_checked & is_staff:
            self._web_driver.click_element(admin_add_user_locator.add_user_staff_check)
        self.select_group(groups)
        self.select_permission(permissions)
        self._web_driver.click_element(admin_add_user_locator.add_user_save_button)
