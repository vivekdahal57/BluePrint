from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddCollectionPage(BasePage):
    add_collection_title_text = (By.XPATH, "//h1[contains(text(),'Add collection')]")
    add_collection_change_collection_title_text = (By.XPATH, "//h1[contains(text(),'Change collection')]")
    add_collection_save_button = (By.NAME, "_save")
    add_collection_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_collection_page(self):
        self._web_driver.verify_text(self.add_collection_title_text, "Add collection")

    def verify_change_collection_page(self):
        self._web_driver.verify_text(self.add_collection_change_collection_title_text,
                                     "Change collection")

    def delete_collection(self):
        self._web_driver.click_element(self.add_collection_delete_button)
        self._web_driver.click_element(self.confirm_delete)