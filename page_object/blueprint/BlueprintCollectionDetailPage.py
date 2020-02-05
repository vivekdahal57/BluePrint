from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintCollectionDetailPage(BasePage):
    dashboard_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    dashboard_collection_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    dashboard_collection_name_text = (By.ID, "collection-header-name")
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_collection_details_page(self, col_name):
        self._web_driver.scroll_to(self.dashboard_collection_name_text)
        self._web_driver.verify_text(self.dashboard_collection_name_text, col_name)
