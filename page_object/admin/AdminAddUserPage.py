import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddUserPage(BasePage):
    add_user_title_text = (By.XPATH, "//h1[contains(text(),'Add user')]")
    add_user_change_user_title_text = (By.XPATH, "//h1[contains(text(),'Change user')]")
    add_user_username_field = (By.ID, "id_username")
    add_user_password1_field = (By.ID, "id_password1")
    add_user_password2_field = (By.ID, "id_password2")
    add_user_save_button = (By.NAME, "_save")
    add_user_first_name_field = (By.ID, "id_first_name")
    add_user_last_name_field = (By.ID, "id_last_name")
    add_user_email_field = (By.ID, "id_email")
    add_user_active_check = (By.ID, "id_is_active")
    add_user_staff_check = (By.ID, "id_is_staff")
    add_user_super_user_check = (By.ID, "id_is_superuser")
    add_user_groups_from_list = (By.ID, "id_groups_from")
    add_user_group_add_arrow_button = (By.ID, "id_groups_add_link")
    add_user_group_remove_arrow_button = (By.ID, "id_groups_remove_link")
    add_user_groups_to_list = (By.ID, "id_groups_to")
    add_user_group_search_text = (By.ID, "id_groups_input")
    add_user_group_option = (By.XPATH, "//*[@name='groups_old']/option[1]")
    add_user_permission_from_list = (By.ID, "id_user_permissions_from")
    add_user_permission_to_list = (By.ID, "id_user_permissions_to")
    add_user_permission_add_arrow_button = (By.ID, "id_groups_add_link")
    add_user_permission_remove_arrow_button = (By.ID, "id_groups_remove_link")
    add_user_permission_search_text = (By.ID, "id_permissions_input")
    add_user_permission_option = (By.XPATH, "//*[@name='user_permissions_old']/option[1]")
    add_user_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_user_page(self):
        self._web_driver.verify_text(self.add_user_title_text, "Add user")

    def verify_change_user_page(self):
        self._web_driver.verify_text(self.add_user_change_user_title_text, "Change user")

    def select_group(self, groups):
        for group in groups:
            self._web_driver.send_value(self.add_user_group_search_text, group)
            time.sleep(2)
            # if self._web_driver.verify_text(self.add_user_group_option, group):
            self._web_driver.double_click_element(self.add_user_group_option)
            # self._web_driver.click_element(self.add_user_group_add_arrow_button)

    def select_permission(self, permissions):
        for permission in permissions:
            self._web_driver.send_value(self.add_user_permission_search_text, permission)
            time.sleep(2)
            # if self._web_driver.verify_text(self.add_user_permission_option, permission):
            self._web_driver.double_click_element(self.add_user_permission_option)
            # self._web_driver.click_element(self.add_user_permission_add_arrow_button)

    def create_user(self, username, password):
        self._web_driver.send_value(self.add_user_username_field, username)
        self._web_driver.send_value(self.add_user_password1_field, password)
        self._web_driver.send_value(self.add_user_password2_field, password)
        self._web_driver.click_element(self.add_user_save_button)
        self.verify_change_user_page()

    def change_user(self, first_name, last_name, email, is_active, is_staff, is_super_user, groups, permissions):
        self._web_driver.send_value(self.add_user_first_name_field, first_name)
        self._web_driver.send_value(self.add_user_last_name_field, last_name)
        self._web_driver.send_value(self.add_user_email_field, email)
        is_checked = self._web_driver.find_element(self.add_user_active_check).is_selected()
        if not is_checked and is_active:
            self._web_driver.click_element(self.add_user_active_check)
        is_checked = self._web_driver.find_element(self.add_user_super_user_check).is_selected()
        if not is_checked and is_super_user:
            self._web_driver.click_element(self.add_user_super_user_check)
        is_checked = self._web_driver.find_element(self.add_user_staff_check).is_selected()
        if not is_checked and is_staff:
            self._web_driver.click_element(self.add_user_staff_check)
        self.select_group(groups)
        self.select_permission(permissions)
        self._web_driver.click_element(self.add_user_save_button)

    def delete_user(self):
        self._web_driver.click_element(self.add_user_delete_button)
        self._web_driver.click_element(self.confirm_delete)
