import time
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class AdminDashboardPage(BasePage):
    _web_driver_wait = None
    dashboard_title_text = (By.XPATH, "//h1[contains(text(),'Site administration')]")
    logout_link = (By.XPATH, "//a[contains(text(),'Log out')]")
    logout_page_title = (By.XPATH, "// h1[contains(text(), 'Logged out')]")
    user_profile_link = (By.XPATH, "//a[contains(text(),'User profiles')]")
    user_link = (By.XPATH, "//a[contains(text(),'Users')]")
    collection_link = (By.XPATH, "//a[contains(text(),'Collections')]")
    cluster_link = (By.XPATH, "//a[contains(text(),'Cluster')]")
    ingest_plans_link = (By.XPATH, "//a[contains(text(),'Ingest plans')]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_pass(self):
        self._web_driver.verify_text(self.dashboard_title_text, 'Site administration')

    def logout(self):
        time.sleep(1)
        self._web_driver.click_element(self.logout_link)
        self.verify_logout_page()

    def verify_logout_page(self):
        self._web_driver.verify_text(self.logout_page_title, "Logged out")

    def goto_users_list(self):
        self._web_driver.scroll_to(self.user_link)
        self._web_driver.click_element(self.user_link)

    def goto_users_profile_list(self):
        self._web_driver.scroll_to(self.user_profile_link)
        self._web_driver.click_element(self.user_profile_link)

    def goto_collection_list(self):
        self._web_driver.scroll_to(self.collection_link)
        self._web_driver.click_element(self.collection_link)

    def goto_cluster_list(self):
        self._web_driver.scroll_to(self.cluster_link)
        self._web_driver.click_element(self.cluster_link)

    def goto_ingest_plans_list(self):
        self._web_driver.scroll_to(self.ingest_plans_link)
        self._web_driver.click_element(self.ingest_plans_link)
