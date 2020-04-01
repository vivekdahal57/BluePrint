from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminGroupsListPage(BasePage):
    group_title_text = (By.XPATH, "//h1[contains(text(),'Select group to change')]")
    group_add_button = (By.XPATH, "//a[@class='addlink']")
    group_change_success = (By.CSS_SELECTOR, "li.success")
    group_search_field = (By.ID, "searchbar")
    group_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    group_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_group_list_page(self):
        self._web_driver.verify_text(self.group_title_text, "Select group to change")

    def goto_add_group_page(self):
        self._web_driver.scroll_to(self.group_add_button)
        self._web_driver.click_element(self.group_add_button)

    def search_and_land_to_change_group(self, group_name):
        self._web_driver.send_value(self.group_search_field, group_name)
        self._web_driver.click_element(self.group_search_button)
        self._web_driver.verify_text(self.group_search_output, group_name, 2)
        self._web_driver.click_element(self.group_search_output)
