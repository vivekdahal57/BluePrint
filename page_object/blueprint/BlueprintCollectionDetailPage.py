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
    collection_detail_rename_btn = (
        By.XPATH, "//button[@class='button button--primary button--desertstorm button--icon-only']")
    collection_detail_reauthenticate_btn = (By.XPATH, "//span[contains(text(),'Reauthenticate')]")
    collection_detail_cancel_download_btn = (By.XPATH, "//button[@class='cancel-download']")
    collection_detail_search_icon = (
        By.XPATH, "//button[@class='button button--primary button--transparent button--icon-only']")
    collection_detail_search_field = (By.XPATH, "//input[@placeholder='Search Here']")
    collection_detail_search_result = (By.XPATH, "//mark[contains(@class,'foundWord')]")
    collection_detail_search_no_result_msg = (By.XPATH, "//p[contains(text(),'No results.')]")
    collection_detail_close_search = (By.XPATH, "//div[@class='closeSearchWindow']")
    collection_detail_check_hidden_box = (By.ID, "collectionCheck")
    collection_detail_check_collection_box = (By.XPATH, "//label[@class='collectionCheckLabel']")
    collection_detail_browse_file_button = (By.XPATH, "//button[@class='upload-content']")
    collection_detail_upload_cancel_btn = (By.XPATH, "//button[@class='cancel-upload']")
    collection_detail_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    collection_detail_collection_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    collection_detail_upload_file_btn = (By.XPATH, "//a[contains(text(),'+ Upload Documents')]")
    collection_detail_ingested_doc_link = (By.XPATH, "//div[@class='cluster-name cluster-name--margin-adjusted']")
    collection_detail_cluster_status_bar = (By.XPATH, "//div[@class='flex-row flex-row--progress']")
    collection_detail_ingesting_progress_bar = (By.XPATH, "//div[@class='processing-queue__filename']")
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def goto_ingested_documents_page(self):
        self._web_driver.click_element(self.collection_detail_ingested_doc_link)

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

    def rename_collection(self, new_name):
        self._web_driver.click_element(self.collection_detail_rename_btn)
        self._web_driver.send_value(self.dashboard_collection_name_popup, new_name)
        self._web_driver.click_element(self.dashboard_collection_ok_button)

    def search_valid_file_and_land(self, search_text, is_active):
        self._web_driver.click_element(self.collection_detail_search_icon)
        time.sleep(1)
        self._web_driver.driver.execute_script(
            "document.querySelector(arguments[0]).setAttribute('style','visibility:visible');",
            "input[id='collectionCheck']")
        is_checked = self._web_driver.find_element(self.collection_detail_check_hidden_box).is_selected()
        if not is_checked and is_active == "True":
            self._web_driver.click_element(self.collection_detail_check_collection_box)
        elif is_checked and not is_active == "True":
            self._web_driver.click_element(self.collection_detail_check_collection_box)
        self._web_driver.send_value(self.collection_detail_search_field, search_text)
        self._web_driver.verify_text(self.collection_detail_search_result, search_text)
        self._web_driver.click_element(self.collection_detail_search_result)

    def search_invalid_file(self, search_text):
        self._web_driver.click_element(self.collection_detail_search_icon)
        self._web_driver.send_value(self.collection_detail_search_field, search_text)
        self._web_driver.verify_text(self.collection_detail_search_no_result_msg, 'No results')
        self._web_driver.click_element(self.collection_detail_close_search)

    def add_file_to_existing_collection(self, file_path, collection_name):
        self._web_driver.click_element(self.collection_detail_upload_file_btn)
        self._web_driver.verify_text(self.collection_detail_browse_file_button, "Browse")
        self._web_driver.upload_file(file_path)
        self._web_driver.find_element(self.collection_detail_upload_cancel_btn, 600)
        self._web_driver.wait_until_element_disappear(self.collection_detail_upload_cancel_btn, 600)

    def verify_cluster_status(self, status_name):
        self._web_driver.verify_text(self.collection_detail_cluster_status_bar, status_name)

    def verify_ingesting_bar(self, file_name):
        self._web_driver.verify_text(self.collection_detail_ingesting_progress_bar, file_name)
        self._web_driver.reload_page()
        time.sleep(1)
