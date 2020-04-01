import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddGroupPage(BasePage):
    add_group_title_text = (By.XPATH, "//h1[contains(text(),'Add group')]")
    add_group_change_group_title_text = (By.XPATH, "//h1[contains(text(),'Change group')]")
    add_group_save_button = (By.NAME, "_save")
    add_group_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")
    add_group_group_name_field = (By.ID, "id_name")
    add_group_all_permission_link = (By.ID, "id_permissions_add_all_link")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_group_page(self):
        self._web_driver.verify_text(self.add_group_title_text, "Add group")

    def verify_change_group_page(self):
        self._web_driver.verify_text(self.add_group_change_group_title_text, "Change group")

    def create_new_group(self, group_name):
        self._web_driver.send_value(self.add_group_group_name_field, group_name)
        self._web_driver.click_element(self.add_group_all_permission_link)
        self._web_driver.click_element(self.add_group_save_button)

    def delete_group(self):
        self._web_driver.click_element(self.add_group_delete_button)
        self._web_driver.click_element(self.confirm_delete)
