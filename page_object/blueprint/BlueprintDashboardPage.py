import time

from selenium.webdriver.common.by import By

from page_object.architect.ArchitectDashboardPage import ArchitectDashboardPage
from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintDashboardPage(BasePage):
    dashboard_title_text = (By.XPATH, "//h2[contains(text(),'All Collections')]")
    dashboard_blueprint_select_half_button = (By.XPATH,
                                              "//div[@class='app-selector__action app-selector__action--blueprint']//button[@class='button button--primary button--min-width app-selector__cta']")
    profile_drop_down = (By.XPATH, "//div[@class='profile']/div[1]")
    logout_link = (By.XPATH, "//span[contains(text(),'Logout')]")
    architect_link = (By.XPATH, "//span[contains(text(),'Switch to Noble Architect')]")
    loading_text = (By.XPATH, "//p[contains(text(),'Loading...')]")
    tos_skip_tour_link = (By.XPATH, "//span[contains(text(),'Skip Tour')]")
    tos_i_agree = (By.XPATH, "//div[@class='form-checkbox__view']")
    tos_agree_continue = (By.XPATH, "//span[contains(text(),'Agree and Continue')]")
    tos_get_started = (By.XPATH, "//span[contains(text(),'Get Started')]")
    dashboard_left_menu_drop_down = (By.XPATH, "//div[@class='left-side']")
    dashboard_left_new_col_button = (By.XPATH, "//span[contains(text(),'+ New Collection')]")
    dashboard_browse_file_button = (By.XPATH, "//button[@class='upload-content']")
    dashboard_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    dashboard_collection_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    dashboard_search_icon = (
        By.XPATH, "//button[@class='button button--primary button--transparent button--icon-only']")
    dashboard_search_field = (By.XPATH, "//input[@placeholder='Search Here']")
    dashboard_search_result = (By.XPATH, "//mark[contains(@class,'foundWord')]")
    dashboard_collection_name_path = "//main[@id='page-wrap']//div//div"

    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)
        self.architect_dashboard_page = ArchitectDashboardPage(obj)

    def get_collection_path_by_name(self, collection_name):
        collection_path = self.dashboard_collection_name_path + "//h3//div[contains(text(),'" + collection_name + "')]"
        elm = (By.XPATH, collection_path)
        return elm

    def get_view_collection_button_path_by_name(self, collection_name):
        view_collection_path = self.dashboard_collection_name_path + "//h3//div[contains(text(),'" + collection_name + "')]//..//..//..//div[3]//a[1]//span[1]"
        print(view_collection_path)
        elm = (By.XPATH, view_collection_path)
        return elm

    def verify_login_pass(self):
        is_present = self._web_driver.does_element_exist(self.dashboard_blueprint_select_half_button)
        if is_present:
            self._web_driver.click_element(self.dashboard_blueprint_select_half_button)
        else:
            self._web_driver.reload_page()
        self._web_driver.verify_text(self.dashboard_title_text, 'All Collections', 120)

    def skip_tour(self, is_accept):
        time.sleep(2)
        is_visible = self._web_driver.does_element_exist(self.tos_skip_tour_link)
        if is_visible:
            self._web_driver.click_element(self.tos_skip_tour_link)
            self.accept_tos_and_continue(is_accept)

    def accept_tos_and_continue(self, is_accept):
        time.sleep(1)
        is_checked = self._web_driver.find_element(self.tos_i_agree).is_selected()
        if not is_checked and is_accept:
            self._web_driver.click_element(self.tos_i_agree)
        self._web_driver.click_element(self.tos_agree_continue)
        self._web_driver.click_element(self.tos_get_started)

    def logout(self):
        self._web_driver.wait_until_element_disappear(self.loading_text)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.logout_link)
        self.blueprint_login_page.verify_login_page()

    def add_new_collection(self, file_path, collection_name):
        time.sleep(1)
        self._web_driver.click_element(self.dashboard_left_menu_drop_down)
        self._web_driver.click_element(self.dashboard_left_new_col_button)
        self.verify_upload_popup()
        self._web_driver.upload_file(file_path)
        self._web_driver.send_value(self.dashboard_collection_name_popup, collection_name)
        self._web_driver.click_element(self.dashboard_collection_ok_button)
        time.sleep(1)
        self._web_driver.reload_page()
        time.sleep(1)

    def verify_upload_popup(self):
        self._web_driver.verify_text(self.dashboard_browse_file_button, "Browse")

    def navigate_to_architect(self):
        self._web_driver.wait_until_element_disappear(self.loading_text)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.architect_link)
        handles = self._web_driver.driver.window_handles
        self._web_driver.driver.switch_to.window(handles[1])
        self.architect_dashboard_page.verify_architect_dashboard()

    def search_and_land(self, search_text):
        self._web_driver.click_element(self.dashboard_search_icon)
        self._web_driver.send_value(self.dashboard_search_field, search_text)
        self._web_driver.verify_text(self.dashboard_search_result, search_text)
        self._web_driver.click_element(self.dashboard_search_result)

    def verify_collection_and_land_on_detail(self, collection_name):
        self._web_driver.verify_text(self.get_collection_path_by_name(collection_name), collection_name)
        self._web_driver.verify_text(self.get_view_collection_button_path_by_name(collection_name), "View Collection")
        self._web_driver.click_element(self.get_view_collection_button_path_by_name(collection_name))
