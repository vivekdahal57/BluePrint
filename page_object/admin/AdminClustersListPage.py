from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminClustersListPage(BasePage):
    cluster_title_text = (By.XPATH, "//h1[contains(text(),'Select cluster to change')]")
    cluster_add_button = (By.XPATH, "//a[@class='addlink']")
    cluster_change_success = (By.CSS_SELECTOR, "li.success")
    cluster_search_field = (By.ID, "searchbar")
    cluster_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    cluster_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_cluster_list_page(self):
        self._web_driver.verify_text(self.cluster_title_text, "Select cluster to change")

    def goto_add_cluster_page(self):
        self._web_driver.scroll_to(self.cluster_add_button)
        self._web_driver.click_element(self.cluster_add_button)

    def search_and_land_to_change_cluster(self, cluster_name):
        self._web_driver.send_value(self.cluster_search_field, cluster_name)
        self._web_driver.click_element(self.cluster_search_button)
        self._web_driver.verify_text(self.cluster_search_output, cluster_name)
        self._web_driver.click_element(self.cluster_search_output)
