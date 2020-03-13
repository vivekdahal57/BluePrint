import time

from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_object.admin.AdminLoginPage import AdminLoginPage
from page_object.base_page import BasePage


class ArchitectIngestPage(BasePage):
    ingest_title_text = (By.XPATH, "//div[contains(text(),'Ingest Plans')]")
    left_menu_drop_down = (By.XPATH, "//img[@class='menu-default']")
    logout_link = (By.XPATH, "//span[contains(text(),'Log Out')]")
    ingest_link = (By.XPATH, "//span[contains(text(),'Ingest')]")
    create_draft_btn = (By.XPATH, "//span[contains(text(),'Create Draft')]")
    ingest_plan_id_drop_down = (By.XPATH, "//div[@class='reactor-dropdown__single-value css-1uccc91-singleValue']")
    ingest_and_activate_button = (By.XPATH, "//span[contains(text(),'Ingest & Activate')]")
    ingest_tree_view_tab = (By.ID, "react-tabs-0")
    ingest_json_tab = (By.ID, "react-tabs-2")
    ingest_step_option = (By.XPATH, "//span[contains(text(),'Steps')]")
    ingest_new_step_title = (By.XPATH, "//h4[contains(text(),'New Step')]")
    ingest_new_step_drop_down = (By.NAME, "new_step_types")
    ingest_new_step_name = (By.NAME, "name")
    ingest_schema_option = (By.XPATH, "//span[contains(text(),'Schema')]")
    ingest_json_input_area = (By.NAME, "plan")
    ingest_plan_create_button = (By.XPATH, "//span[contains(text(),'Create')]")
    ingest_and_activate_button = (By.XPATH, "//span[contains(text(),'Ingest & Activate')]")
    ingest_unstage_expand_icon = (By.XPATH, "//div[@class='ingest-cluster-files']/ul[@class='rc-tree']/li[1]/span[1]")
    ingest_ingested_expand_icon = (By.XPATH, "//div[@class='ingest-cluster-files']/ul[@class='rc-tree']/li[3]/span[1]")
    ingest_unstaged_staged_path = "//span"
    ingest_right_click_stage_btn = (By.XPATH, "//span[@class='button__content'][contains(text(),'Stage')]")
    ingest_files_tab = (By.XPATH, "//div[contains(text(),'Files')]")

    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.admin_login_page = AdminLoginPage(obj)

    def get_staged_unstaged_path(self, file_name):
        return self.ingest_unstaged_staged_path + "[contains(text(),'" + file_name + "')]"

    def verify_ingest_dashboard(self):
        self._web_driver.verify_text(self.ingest_title_text, 'Ingest Plans')

    def expand_collection(self, collection_name):
        collection_path = "//span[contains(text(), '" + collection_name + "')]"
        collection_menu = (By.XPATH, collection_path)
        element = self._web_driver.find_element(collection_menu, 120)
        self._web_driver.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        expand_icon = (By.XPATH, collection_path + "//..//..//span[1]")
        self._web_driver.click_element(expand_icon)

    def select_cluster(self, cluster_name):
        cluster_path = "//span[contains(text(),'" + cluster_name + "')]"
        cluster_ele = (By.XPATH, cluster_path)
        self._web_driver.click_element(cluster_ele)

    def select_cluster_and_create_draft(self, cluster_name):
        self.select_cluster(cluster_name)
        self._web_driver.verify_text(self.create_draft_btn, "Create Draft")
        self._web_driver.click_element(self.create_draft_btn)

    def verify_ingest_draft_plan(self):
        self._web_driver.verify_text(self.ingest_plan_id_drop_down, "(Draft)")

    def make_file_staged(self, file_name):
        self._web_driver.click_element(self.ingest_files_tab)
        file_ele = (By.XPATH, self.get_staged_unstaged_path(file_name))
        self._web_driver.click_element(self.ingest_unstage_expand_icon)
        self._web_driver.click_element(file_ele)
        self.action().context_click(self.find_element(file_ele)).perform()
        self._web_driver.click_element(self.ingest_right_click_stage_btn)

    def create_new_step(self, step_type, step_name):
        self._web_driver.click_element(self.ingest_tree_view_tab)
        self._web_driver.click_element(self.ingest_step_option)
        self._web_driver.verify_text(self.ingest_new_step_title, "New Step")
        self._web_driver.select_value_from_options(self.ingest_new_step_drop_down, step_type)
        self._web_driver.find_element(self.ingest_new_step_name)
        self._web_driver.send_value(self.ingest_new_step_name, step_name)
        self._web_driver.click_element(self.ingest_plan_create_button)
        self._web_driver.click_element(self.ingest_json_tab)
        self._web_driver.send_value(self.ingest_json_input_area,
                                    "{\"steps\": [{\"step_type\": \"FixedBoundingBoxStep\",\"name\": \"bbox - label1\",\"unpack_file_part\": \"0\",\"x\": \"0.1\",\"y\": \"0.2\",\"w\": \"0.4\",\"h\": \"0.05\",\"next_steps\": [{\"step_type\": \"CreateDataAtomStep\",\"name\": \"atom - label1\",\"data_label_name\": \"label1\"}]}],\"schema\": {\"data_labels\": [{\"name\": \"label1\",\"displayName\": \"label1\",\"type\": \"STRING\"}]}}")
        self._web_driver.click_element(self.ingest_and_activate_button)

    def verify_ingested_file(self, file_name):
        file_ele = (By.XPATH, self.get_staged_unstaged_path(file_name))
        time.sleep(3)
        self._web_driver.click_element(self.ingest_ingested_expand_icon)
        self.find_element(file_ele)
