from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminAddUserProfilePage(BasePage):
    add_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    add_profile_change_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    add_profile_company_field = (By.ID, "id_company")
    add_profile_image_browse = (By.ID, "id_picture")
    add_profile_users_dropdown = (By.ID, "id_user")
    add_profile_agreed_tos_check = (By.ID, "id_agreed_terms_of_service")
    add_profile_blueprint_tour_check = (By.ID, "id_has_toured_blueprint")
    add_profile_reactor_tour_check = (By.ID, "id_has_toured_reactor")
    add_profile_multiple_login_check = (By.ID, "id_allow_multiple_login")
    add_profile_save_button = (By.NAME, "_save")
    add_profile_delete_button = (By.XPATH, "//a[@class='deletelink']")

    @staticmethod
    def select_user(username):
        return "//*[@id='id_user']/option[contains(text(),'" + username + "')]"

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_user_profile_page(self):
        self._web_driver.verify_text(self.add_profile_title_text, "Add user profile")

    def verify_change_user_page(self):
        self._web_driver.verify_text(self.add_profile_change_profile_title_text,
                                     "Change user profile")

    def add_user_profile(self, company, username, profile_picture, has_agreed_tos, has_toured_blueprint,
                         has_toured_reactor, is_multiple_login):
        self._web_driver.send_value(self.add_profile_company_field, company)
        if profile_picture != "":
            self._web_driver.send_value(self.add_profile_image_browse, profile_picture)
        self._web_driver.select_value_from_options(self.add_profile_users_dropdown, username)
        is_checked = self._web_driver.find_element(
            self.add_profile_agreed_tos_check).is_selected()
        if not is_checked and has_agreed_tos:
            self._web_driver.click_element(self.add_profile_agreed_tos_check)
        is_checked = self._web_driver.find_element(
            self.add_profile_blueprint_tour_check).is_selected()
        if not is_checked and has_toured_blueprint:
            self._web_driver.click_element(self.add_profile_blueprint_tour_check)
        is_checked = self._web_driver.find_element(
            self.add_profile_reactor_tour_check).is_selected()
        if not is_checked and has_toured_reactor:
            self._web_driver.click_element(self.add_profile_reactor_tour_check)
        is_checked = self._web_driver.find_element(
            self.add_profile_multiple_login_check).is_selected()
        if not is_checked and is_multiple_login:
            self._web_driver.click_element(self.add_profile_multiple_login_check)
        self._web_driver.click_element(self.add_profile_save_button)
