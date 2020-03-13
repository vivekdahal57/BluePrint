import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintCollectionDetailPage(BasePage):
    dashboard_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    dashboard_collection_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    dashboard_collection_name_text = (By.ID, "collection-header-name")
    dashboard_cluster_name_text = (By.XPATH, "//div[@class='cluster-name']//h3")
    collection_detail_download_btn = (By.XPATH, "//span[contains(text(),'Download All Structured Data')]")
    collection_detail_password_field = (By.NAME, "password")
    collection_detail_reauthenticate_btn = (By.XPATH, "//span[contains(text(),'Reauthenticate')]")
    collection_detail_cancel_download_btn = (By.XPATH, "//button[@class='cancel-download']")
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_collection_details_page(self, col_name):
        self._web_driver.scroll_to(self.dashboard_collection_name_text)
        self._web_driver.verify_text(self.dashboard_collection_name_text, col_name)

    def verify_cluster_name(self, cluster_name):
        self._web_driver.verify_text(self.dashboard_cluster_name_text, cluster_name)

    def download_structured_file(self):
        self._web_driver.click_element(self.collection_detail_download_btn)
        self._web_driver.send_value(self.collection_detail_password_field, "Winter20")
        self._web_driver.find_element(self.collection_detail_reauthenticate_btn).click()
        time.sleep(1)
        self._web_driver.wait_until_element_disappear(self.collection_detail_cancel_download_btn, 120)
