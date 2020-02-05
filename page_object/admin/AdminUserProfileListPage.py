from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminUserProfileListPage(BasePage):
    user_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    user_profile_add_profile_button = (By.XPATH, "//*[@id='content-main']/ul/li[1]/a")
    user_profile_search_field = (By.ID, "searchbar")
    user_profile_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    user_profile_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
    user_profile_change_success = (By.XPATH, "//li[@class='success']")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_user_profile_page(self):
        self._web_driver.verify_text(self.user_profile_title_text,
                                     "Select user profile to change")

    def goto_add_user_profile_page(self):
        self._web_driver.scroll_to(self.user_profile_add_profile_button)
        self._web_driver.click_element(self.user_profile_add_profile_button)

    def verify_user_profile_change_success(self, username):
        self._web_driver.verify_text(self.user_profile_change_success,
                                     "The user profile " + username + " was changed successfully.")

    def search_and_land_to_change_user_profile(self, username):
        self._web_driver.send_value(admin_users_list_locator.user_search_field, username)
        self._web_driver.click_element(admin_users_list_locator.user_search_button)
        self._web_driver.verify_text(admin_users_list_locator.user_search_output, username)
        self._web_driver.click_element(admin_users_list_locator.user_search_output)
