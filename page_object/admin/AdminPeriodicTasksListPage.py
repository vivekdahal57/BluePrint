import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminPeriodicTasksListPage(BasePage):
    periodic_task_title_text = (By.XPATH, "//h1[contains(text(),'Select periodic task to change')]")
    periodic_task_add_button = (By.XPATH, "//a[@class='addlink']")
    periodic_task_change_success = (By.CSS_SELECTOR, "li.success")
    periodic_task_search_field = (By.ID, "searchbar")
    periodic_task_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    periodic_task_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
    periodic_task_first_row_select = (By.XPATH, "//tr[1]//input[@name='_selected_action']")
    periodic_task_action_drop_down = (By.NAME, "action")
    periodic_task_go_button = (By.NAME, "index")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_periodic_task_list_page(self):
        self._web_driver.verify_text(self.periodic_task_title_text, "Select periodic task to change")

    def goto_add_periodic_task_page(self):
        self._web_driver.scroll_to(self.periodic_task_add_button)
        self._web_driver.click_element(self.periodic_task_add_button)

    def search_and_land_to_change_periodic_task(self, periodic_task_name):
        self._web_driver.send_value(self.periodic_task_search_field, periodic_task_name)
        self._web_driver.click_element(self.periodic_task_search_button)
        self._web_driver.verify_text(self.periodic_task_search_output, periodic_task_name, 2)
        self._web_driver.click_element(self.periodic_task_search_output)

    def search_and_run_periodic_task(self, periodic_task_name):
        self._web_driver.send_value(self.periodic_task_search_field, periodic_task_name)
        self._web_driver.click_element(self.periodic_task_search_button)
        self._web_driver.verify_text(self.periodic_task_search_output, periodic_task_name, 2)
        self._web_driver.click_element(self.periodic_task_first_row_select)
        self._web_driver.select_value_from_options(self.periodic_task_action_drop_down, "Run selected tasks")
        time.sleep(2)
        self._web_driver.click_element(self.periodic_task_go_button)
        time.sleep(2)
