import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintClusterDetailPage(BasePage):
    cluster_detail_title_text = (By.ID, "cluster-detail-name")
    cluster_detail_rename_btn = (
        By.XPATH, "//button[@class='button button--primary button--white button--icon-only cluster-actions__button']")
    cluster_detail_rename_field = (By.XPATH, "//input[@class='textInput']")
    cluster_detail_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    cluster_detail_search_icon = (
        By.XPATH, "//button[@class='button button--primary button--transparent button--icon-only']")
    cluster_detail_search_field = (By.XPATH, "//input[@placeholder='Search Here']")
    cluster_detail_search_result = (By.XPATH, "//mark[contains(@class,'foundWord')]")
    cluster_detail_search_no_result_msg = (By.XPATH, "//p[contains(text(),'No results.')]")
    cluster_detail_close_search = (By.XPATH, "//div[@class='closeSearchWindow']")
    cluster_detail_col_check_hidden_box = (By.ID, "collectionCheck")
    cluster_detail_cluster_check_hidden_box = (By.ID, "clusterCheck")
    cluster_detail_check_collection_box = (By.XPATH, "//label[@class='collectionCheckLabel']")
    cluster_detail_check_cluster_box = (By.XPATH, "//label[@class='clusterCheckLabel']")
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_cluster_details_page(self, cluster_name):
        self._web_driver.scroll_to(self.cluster_detail_title_text)
        self._web_driver.verify_text(self.cluster_detail_title_text, cluster_name)

    def rename_cluster(self, new_name):
        self._web_driver.click_element(self.cluster_detail_rename_btn)
        self._web_driver.send_value(self.cluster_detail_rename_field, new_name)
        self._web_driver.click_element(self.cluster_detail_ok_button)

    def search_valid_file_and_land(self, search_text, is_col_active, is_cluster_active):
        self._web_driver.click_element(self.cluster_detail_search_icon)
        self._web_driver.driver.execute_script(
            "document.querySelector(arguments[0]).setAttribute('style','visibility:visible');",
            "input[id='collectionCheck']")
        time.sleep(1)
        self._web_driver.driver.execute_script(
            "document.querySelector(arguments[0]).setAttribute('style','visibility:visible');",
            "input[id='clusterCheck']")
        is_checked = self._web_driver.find_element(self.cluster_detail_col_check_hidden_box).is_selected()
        if not is_checked and is_col_active == "True":
            self._web_driver.click_element(self.cluster_detail_check_collection_box)
        elif is_checked and not is_col_active == "True":
            self._web_driver.click_element(self.cluster_detail_check_collection_box)
        is_checked = self._web_driver.find_element(self.cluster_detail_cluster_check_hidden_box).is_selected()
        if not is_checked and is_cluster_active == "True":
            self._web_driver.click_element(self.cluster_detail_check_cluster_box)
        elif is_checked and not is_cluster_active == "True":
            self._web_driver.click_element(self.cluster_detail_check_cluster_box)
        self._web_driver.send_value(self.cluster_detail_search_field, search_text)
        self._web_driver.verify_text(self.cluster_detail_search_result, search_text)
        self._web_driver.click_element(self.cluster_detail_search_result)
        self._web_driver.reload_page()

    def search_invalid_file(self, search_text):
        self._web_driver.click_element(self.cluster_detail_search_icon)
        self._web_driver.send_value(self.cluster_detail_search_field, search_text)
        self._web_driver.verify_text(self.cluster_detail_search_no_result_msg, 'No results')
        self._web_driver.click_element(self.cluster_detail_close_search)
