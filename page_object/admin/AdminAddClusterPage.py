from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddClusterPage(BasePage):
    add_cluster_title_text = (By.XPATH, "//h1[contains(text(),'Add cluster')]")
    add_cluster_change_cluster_title_text = (By.XPATH, "//h1[contains(text(),'Change cluster')]")
    add_cluster_name_field = (By.ID, "id_name")
    add_cluster_collection_select_id = 'id_collection'
    add_cluster_status_select = (By.ID, "id_status")
    add_cluster_save_button = (By.NAME, "_save")
    add_cluster_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_cluster_page(self):
        self._web_driver.verify_text(self.add_cluster_title_text, "Add cluster")

    def verify_change_cluster_page(self):
        self._web_driver.verify_text(self.add_cluster_change_cluster_title_text,
                                     "Change cluster")

    def create_or_change_cluster(self, cluster_name, collection_name, status):
        self._web_driver.send_value(self.add_cluster_name_field, cluster_name)
        self._web_driver.select_value_from_options(self.add_cluster_status_select, status)
        self._web_driver.select_value_by_partial_text_options(
            self.add_cluster_collection_select_id, collection_name)
        self._web_driver.click_element(self.add_cluster_save_button)

    def delete_cluster(self):
        self._web_driver.click_element(self.add_cluster_delete_button)
        self._web_driver.click_element(self.confirm_delete)
