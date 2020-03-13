import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminIngestResultsListPage(BasePage):
    ingest_result_title_text = (By.XPATH, "//h1[contains(text(),'Select ingest result to change')]")
    ingest_result_change_title_text = (By.XPATH, "//h1[contains(text(),'Change ingest result')]")
    ingest_result_add_button = (By.XPATH, "//a[@class='addlink']")
    ingest_result_change_success = (By.CSS_SELECTOR, "li.success")
    ingest_result_search_field = (By.ID, "searchbar")
    ingest_result_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    ingest_result_search_output = (By.XPATH, "//table[@id='result_list']//tbody//tr[1]//th[1]//a")
    ingest_result_search_result = (By.XPATH, "//table[@id='result_list']//tbody//tr[1]//td[4]")
    ingest_result_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")
    ingest_result_search_col_temp_path = "//table[@id='result_list']//tbody//tr//td"
    plan_name = None

    def __init__(self, obj):
        self._web_driver = obj

    def get_search_path(self, plan_name):
        path = self.ingest_result_search_col_temp_path + "[contains(text(),'" + plan_name + "')]"
        return path

    def verify_ingest_result_list_page(self):
        self._web_driver.verify_text(self.ingest_result_title_text, "Select ingest result to change")

    def goto_add_ingest_result_page(self):
        self._web_driver.scroll_to(self.ingest_result_add_button)
        self._web_driver.click_element(self.ingest_result_add_button)

    def search_and_confirm_completed_ingest_result(self):
        path = self.get_search_path(self.plan_name)
        elm = (By.XPATH, path)
        self._web_driver.verify_text(elm, self.plan_name)
        elm = (By.XPATH, path + "//..//td[3]")
        self._web_driver.verify_text(elm, "Complete")

    def verify_ingest_result_change_page(self):
        self._web_driver.verify_text(self.ingest_change_title_text, "Change ingest result")

    def delete_ingest_result(self):
        self._web_driver.click_element(self.ingest_result_delete_button)
        self._web_driver.click_element(self.confirm_delete)
