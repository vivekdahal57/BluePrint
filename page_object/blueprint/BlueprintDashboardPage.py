import time

from selenium.common.exceptions import TimeoutException
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
    user_manual_link = (By.XPATH, "//span[contains(text(),'User Manual')]")
    faq_link = (By.XPATH, "//span[contains(text(),'FAQ')]")
    terms_of_service_link = (By.XPATH, "//span[contains(text(),'Terms of Service')]")
    loading_text = (By.XPATH, "//p[contains(text(),'Loading...')]")
    tos_skip_tour_link = (By.XPATH, "//span[contains(text(),'Skip Tour')]")
    tos_i_agree = (By.XPATH, "//div[@class='form-checkbox__view']")
    tos_agree_continue = (By.XPATH, "//span[contains(text(),'Agree and Continue')]")
    tos_get_started = (By.XPATH, "//span[contains(text(),'Get Started')]")
    dashboard_left_menu_drop_down = (By.XPATH, "//div[@class='left-side']")
    dashboard_left_new_col_button = (By.XPATH, "//span[contains(text(),'+ New Collection')]")
    dashboard_browse_file_button = (By.XPATH, "//button[@class='upload-content']")
    dashboard_upload_cancel_btn = (By.XPATH, "//button[@class='cancel-upload']")
    dashboard_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    dashboard_collection_ok_button = (
        By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    dashboard_search_icon = (
        By.XPATH, "//button[@class='button button--primary button--transparent button--icon-only']")
    dashboard_search_field = (By.XPATH, "//input[@placeholder='Search Here']")
    dashboard_search_result = (By.XPATH, "//mark[contains(@class,'foundWord')]")
    dashboard_collection_name_path = "//main[@id='page-wrap']//div//div"
    dashboard_sort_by_drop_down = (By.XPATH, "//div[@class='sortDropdownWrapper']")
    dashboard_sort_old_new = (By.XPATH, "//li[contains(text(),'CREATED DATE (OLD to NEW)')]")
    dashboard_sort_new_old = (By.XPATH, "//li[contains(text(),'CREATED DATE (NEW to OLD)')]")
    dashboard_sort_high_low = (By.XPATH, "//li[contains(text(),'CERTAINTY SCORE (HIGH to LOW)')]")
    dashboard_sort_low_high = (By.XPATH, "//li[contains(text(),'CERTAINTY SCORE (LOW to HIGH)')]")
    dashboard_collection_number = (By.XPATH, "//div[@class='dashboard__preview-modules']//div[1]//div[1]//h3[1]/div[1]")
    dashboard_upload_error = (By.XPATH, "//span[@class='info info--error']")
    user_manual_component_text = (By.XPATH, "//a[contains(text(),'1. Create or Select Existing Collection')]")
    faq_title_text = (By.XPATH, "//h2[contains(text(),'Frequently Asked Questions')]")
    terms_of_service_text = (By.XPATH, "//a[contains(text(),'click here')]")
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
        view_collection_path = self.dashboard_collection_name_path + "//h3//div[contains(text(),'" + collection_name + "')]//..//..//..//div[3]//a[1]//span[contains(text(),'View Collection')]"
        elm = (By.XPATH, view_collection_path)
        return elm

    def verify_login_pass(self):
        is_present = self._web_driver.does_element_exist(self.dashboard_blueprint_select_half_button)
        if is_present:
            self._web_driver.click_element(self.dashboard_blueprint_select_half_button)
        else:
            self._web_driver.reload_page()
        url = self._web_driver.get_current_url()
        if "reactor" in url.split("/"):
            self._web_driver.open(url.replace("reactor", "blueprint"))
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
        handles = self._web_driver.driver.window_handles
        for x in range(len(handles), 0, -1):
            time.sleep(1)
            self._web_driver.driver.switch_to.window(handles[x - 1])
            if x != 1:
                self._web_driver.driver.close()

        self._web_driver.wait_until_element_disappear(self.loading_text, 120)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.logout_link)
        self.blueprint_login_page.verify_login_page()

    def upload_preparation(self, file_path):
        time.sleep(1)
        self._web_driver.click_element(self.dashboard_left_menu_drop_down)
        self._web_driver.click_element(self.dashboard_left_new_col_button)
        self.verify_upload_popup()
        self._web_driver.upload_file(file_path)
        is_error = self._web_driver.does_element_exist(self.dashboard_upload_error)
        flag = None
        if is_error:
            error_msg = self._web_driver.get_text(self.dashboard_upload_error)
            for value in ['Error: Max upload size exceeds 2 GB.', 'Cannot upload empty file.',
                          'File type not supported.']:
                try:
                    assert error_msg in value, "not this error" + error_msg
                    flag = True
                    break
                except AssertionError:
                    flag = False
            if not flag:
                raise ValueError('Unknown error message visible')
            return False
        else:
            return True

    def add_new_collection(self, file_path, collection_name):
        if self.upload_preparation(file_path):
            time.sleep(1)
            self._web_driver.wait_until_element_disappear(self.dashboard_upload_cancel_btn, 600)
            self._web_driver.send_value(self.dashboard_collection_name_popup, collection_name)
            self._web_driver.click_element(self.dashboard_collection_ok_button)

    def upload_and_cancel_in_10s(self, file_path):
        if self.upload_preparation(file_path):
            time.sleep(4)
            self._web_driver.close_current_tab_and_switch_to_old()

    def upload_and_click_back(self, file_path):
        if self.upload_preparation(file_path):
            time.sleep(4)
            self._web_driver.driver.back()

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

    def search_collection_till_not_found(self, collection_name):
        try:
            self._web_driver.verify_text(self.get_collection_path_by_name(collection_name), collection_name, 2)
            assert False, 'Collection is visible'
        except TimeoutException:
            assert True

    def sort_by_and_verify(self, sort_criteria):
        self._web_driver.scroll_to(self.dashboard_sort_by_drop_down)
        if sort_criteria == "old to new":
            self._web_driver.click_element(self.dashboard_sort_old_new)
        elif sort_criteria == "new to old":
            self._web_driver.click_element(self.dashboard_sort_new_old)
        elif sort_criteria == "high to low":
            self._web_driver.click_element(self.dashboard_sort_high_low)
        elif sort_criteria == "low to high":
            self._web_driver.click_element(self.dashboard_sort_low_high)
        time.sleep(2)

    def navigate_to_user_manual(self):
        self._web_driver.wait_until_element_disappear(self.loading_text)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.user_manual_link)
        time.sleep(1)
        handles = self._web_driver.driver.window_handles
        self._web_driver.driver.switch_to.window(handles[1])
        self._web_driver.verify_text(self.user_manual_component_text, "Create or Select Existing Collection")

    def navigate_to_faq(self):
        self._web_driver.wait_until_element_disappear(self.loading_text)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.faq_link)
        time.sleep(1)
        handles = self._web_driver.driver.window_handles
        self._web_driver.driver.switch_to.window(handles[1])
        self._web_driver.verify_text(self.faq_title_text, "Frequently Asked Questions")

    def navigate_to_terms_of_service(self):
        self._web_driver.wait_until_element_disappear(self.loading_text)
        self._web_driver.scroll_to(self.profile_drop_down)
        self._web_driver.click_element(self.terms_of_service_link)
        time.sleep(1)
        handles = self._web_driver.driver.window_handles
        self._web_driver.driver.switch_to.window(handles[1])
        self._web_driver.verify_text(self.terms_of_service_text, "click here")

    def navigate_to_google_analytics(self):
        self._web_driver.click_element(self.terms_of_service_text)
        time.sleep(1)
        handles = self._web_driver.driver.window_handles
        self._web_driver.driver.switch_to.window(handles[2])
        if self._web_driver.get_current_url() != 'https://policies.google.com/technologies/partner-sites':
            raise ValueError(self._web_driver.get_current_url())
