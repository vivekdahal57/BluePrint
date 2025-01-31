import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_object.admin.AdminLoginPage import AdminLoginPage
from page_object.base_page import BasePage


class ArchitectDashboardPage(BasePage):
    dashboard_title_text = (By.XPATH, "//h3[contains(text(),'Organize')]")
    left_menu_drop_down = (By.XPATH, "//img[@class='menu-default']")
    logout_link = (By.XPATH, "//a[contains(text(),'Log Out')]")
    ingest_link = (By.XPATH, "//a[contains(text(),'Ingest')]")
    expand_link = (By.XPATH, "//span[contains(text(),'Expand')]")
    collections_drop_down = (By.XPATH, "//div[@class='reactor-dropdown__indicators css-1wy0on6']")
    collections_menu_path = "//div[@class='reactor-dropdown__menu css-26l3qy-menu']//div//div"
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.admin_login_page = AdminLoginPage(obj)

    def verify_architect_dashboard(self):
        self._web_driver.verify_text(self.dashboard_title_text, 'Organize')

    def select_collection(self, collection_name):
        path = self.collections_menu_path + "[contains(text(),'" + collection_name + "')]"
        collection_menu = (By.XPATH, path)
        self._web_driver.find_element(self.expand_link, 120)
        self._web_driver.find_element(self.collections_drop_down).click()
        self._web_driver.driver.execute_script("arguments[0].scrollIntoView(true);", self.find_element(collection_menu))
        self._web_driver.click_element(collection_menu)

    def drag_transfer_batch_to_cluster(self, cluster_name):
        draggable = (By.CSS_SELECTOR, ".rc-tree-node-selected.draggable")
        draggable_before = (By.XPATH, "//span[contains(text(),'TransferBatch:')]")
        cluster_elm = (By.XPATH, "//span[@title='Cluster: " + cluster_name + "']")
        # self._web_driver.change_height(self._web_driver.find_element(cluster_elm), 100)
        self._web_driver.scroll_to(draggable_before)
        self._web_driver.click_element(draggable_before)
        time.sleep(2)
        self._web_driver.drag_from_drop_to_js(draggable, cluster_elm)
        self._web_driver.wait_until_element_disappear(draggable_before)

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

    def go_to_ingest_page(self):
        self._web_driver.scroll_to(self.left_menu_drop_down)
        self._web_driver.click_element(self.ingest_link)
        time.sleep(1)
