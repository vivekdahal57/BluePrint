from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminCollectionsListPage(BasePage):
    collection_title_text = (By.XPATH, "//h1[contains(text(),'Select collection to change')]")
    collection_add_button = (By.XPATH, "//a[@class='addlink']")
    collection_change_success = (By.CSS_SELECTOR, "li.success")
    collection_search_field = (By.ID, "searchbar")
    collection_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    collection_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_collections_list_page(self):
        self._web_driver.verify_text(self.collection_title_text, "Select collection to change")

    def goto_add_collection_page(self):
        self._web_driver.scroll_to(self.collection_add_button)
        self._web_driver.click_element(self.collection_add_button)

    def search_and_land_to_change_collection(self, collection_name):
        self._web_driver.send_value(self.collection_search_field, collection_name)
        self._web_driver.click_element(self.collection_search_button)
        self._web_driver.verify_text(self.collection_search_output, collection_name, 2)
        self._web_driver.click_element(self.collection_search_output)
