from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminUsersListPage(BasePage):
    user_title_text = (By.XPATH, "//h1[contains(text(),'Select user to change')]")
    user_add_button = (By.XPATH, "//a[@class='addlink']")
    user_change_success = (By.CSS_SELECTOR, "li.success")
    user_search_field = (By.ID, "searchbar")
    user_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    user_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_users_list_page(self):
        self._web_driver.verify_text(self.user_title_text, "Select user to change")

    def goto_add_user_page(self):
        self._web_driver.scroll_to(self.user_add_button)
        self._web_driver.click_element(self.user_add_button)

    def verify_user_change_success(self, username):
        self._web_driver.verify_text(self.user_change_success,
                                     "The user " + username + " was changed successfully.")

    def search_and_land_to_change_user(self, username):
        self._web_driver.send_value(self.user_search_field, username)
        self._web_driver.click_element(self.user_search_button)
        self._web_driver.verify_text(self.user_search_output, username)
        self._web_driver.click_element(self.user_search_output)
