import time

from selenium.webdriver.common.by import By

from page_object.admin.AdminLoginPage import AdminLoginPage
from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class ArchitectDashboardPage(BasePage):
    dashboard_title_text = (By.XPATH, "//h3[contains(text(),'Organize')]")
    left_menu_drop_down = (By.XPATH, "//img[@class='menu-default']")
    logout_link = (By.XPATH, "//span[contains(text(),'Log Out')]")
    expand_link = (By.XPATH, "//span[contains(text(),'Expand')]")
    collections_drop_down = (By.NAME, "collections")
    transfer_batch_cluster_list_path = "//main[@id='page-wrap']//li"
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.admin_login_page = AdminLoginPage(obj)

    def verify_architect_dashboard(self):
        self._web_driver.verify_text(self.dashboard_title_text, 'Organize')

    def select_collection(self, collection_name):
        self._web_driver.find_element(self.expand_link, 120)
        self._web_driver.click_element(self.collections_drop_down)
        time.sleep(3)
        # self._web_driver.scroll_to((By.XPATH, "//option[contains(text(),'Patents test sdC')]"))
        element = self._web_driver.find_element(By.XPATH,
                                                "//option[contains(text(),'Patents test sdC')]")
        self._web_driver.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self._web_driver.click_element((By.XPATH, "//option[contains(text(),'Patents test sdC')]"))
        time.sleep(5)
        # self._web_driver.select_value_from_options(self.collections_drop_down, collection_name)

    def get_transfer_batch_count(self):
        elms = self._web_driver.find_elements((By.XPATH, self.transfer_batch_cluster_list_path))
        count = 0
        for elm in elms:
            if elm.get_text() in "TransferBatch:":
                count = count + 1
        return count

    def logout(self):
        self._web_driver.scroll_to(self.left_menu_drop_down)
        self._web_driver.click_element(self.logout_link)
        time.sleep(1)
        handles = self._web_driver.driver.window_handles
        for x in range(len(handles), 0, -1):
            self._web_driver.driver.switch_to.window(handles[x - 1])
            if x == len(handles):
                self.admin_login_page.verify_login_page()
            if x != 1:
                self._web_driver.driver.close()
            time.sleep(1)
