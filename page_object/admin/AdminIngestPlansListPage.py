import time

from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminIngestPlansListPage(BasePage):
    ingest_title_text = (By.XPATH, "//h1[contains(text(),'Select ingest plan to change')]")
    ingest_change_title_text = (By.XPATH, "//h1[contains(text(),'Change ingest plan')]")
    ingest_add_button = (By.XPATH, "//a[@class='addlink']")
    ingest_change_success = (By.CSS_SELECTOR, "li.success")
    ingest_search_field = (By.ID, "searchbar")
    ingest_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    ingest_search_output = (By.XPATH, "//table[@id='result_list']//tbody//tr[1]//th[1]//a")
    ingest_search_col_temp_path = "//table[@id='result_list']//tbody//tr//td"
    # //table[@id='result_list']//tbody//tr//td[contains(text(),'automation_cluster1')]//..//th//a
    ingest_plan_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self, obj):
        self._web_driver = obj

    def get_search_path(self, cluster_name):
        path = self.ingest_search_col_temp_path + "[contains(text(),'" + cluster_name + "')]"
        return path

    def verify_ingest_plan_list_page(self):
        self._web_driver.verify_text(self.ingest_title_text, "Select ingest plan to change")

    def goto_add_ingest_plan_page(self):
        self._web_driver.scroll_to(self.ingest_add_button)
        self._web_driver.click_element(self.ingest_add_button)

    def search_and_land_to_change_ingest_plan(self, cluster_name):
        # self._web_driver.send_value(self.cluster_search_field, cluster_name)
        # self._web_driver.click_element(self.cluster_search_button)
        elm = (By.XPATH, self.get_search_path(cluster_name))
        clk_ele = (By.XPATH, self.get_search_path(cluster_name) + "//..//th//a")
        self._web_driver.verify_text(elm, cluster_name)
        self._web_driver.click_element(clk_ele)

    def verify_ingest_plan_change_page(self):
        self._web_driver.verify_text(self.ingest_change_title_text, "Change ingest plan")

    def delete_ingest_plan(self):
        self._web_driver.click_element(self.ingest_plan_delete_button)
        self._web_driver.click_element(self.confirm_delete)
