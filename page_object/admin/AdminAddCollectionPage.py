from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddCollectionPage(BasePage):
    add_collection_title_text = (By.XPATH, "//h1[contains(text(),'Add collection')]")
    add_collection_change_collection_title_text = (By.XPATH, "//h1[contains(text(),'Change collection')]")
    add_collection_add_permission_link = (By.XPATH, "//a[@class='permissionslink']")
    add_collection_add_permission_title_text = (By.XPATH, "//h1[contains(text(),'Object permissions')]")
    add_collection_group_text_field = (By.ID, "id_group")
    add_collection_manage_group_button = (By.NAME, "submit_manage_group")
    add_collection_add_all_permission_link = (By.ID, "id_permissions_add_all_link")
    add_collection_add_all_permission_text = (By.XPATH, "//label[contains(text(),'Permissions:')]")
    add_collection_save_button = (By.NAME, "_save")
    add_collection_add_group_save_button = (By.ID, "submit")
    add_collection_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_collection_page(self):
        self._web_driver.verify_text(self.add_collection_title_text, "Add collection")

    def verify_change_collection_page(self):
        self._web_driver.verify_text(self.add_collection_change_collection_title_text,
                                     "Change collection")

    def assign_group_to_collection(self, group_name):
        self._web_driver.click_element(self.add_collection_add_permission_link)
        self._web_driver.verify_text(self.add_collection_add_permission_title_text, "Object permissions")
        self._web_driver.send_value(self.add_collection_group_text_field, group_name)
        self._web_driver.click_element(self.add_collection_manage_group_button)
        self._web_driver.verify_text(self.add_collection_add_all_permission_text, "Permissions")
        self._web_driver.click_element(self.add_collection_add_all_permission_link)
        self._web_driver.click_element(self.add_collection_add_group_save_button)

    def delete_collection(self):
        self._web_driver.click_element(self.add_collection_delete_button)
        self._web_driver.click_element(self.confirm_delete)
