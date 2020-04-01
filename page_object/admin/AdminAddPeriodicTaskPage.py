import time

from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


def get_future_time(additional_minutes):
    seconds = time.time()
    future_time = time.localtime(seconds + (additional_minutes * 60))
    return time.strftime("%H:%M:%S", future_time)


class AdminAddPeriodicTaskPage(BasePage):
    add_periodic_task_title_text = (By.XPATH, "//h1[contains(text(),'Add periodic task')]")
    add_periodic_task_change_periodic_task_title_text = (By.XPATH, "//h1[contains(text(),'Change periodic task')]")
    add_periodic_task_save_button = (By.NAME, "_save")
    add_periodic_task_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")
    add_periodic_task_name_field = (By.ID, "id_name")
    add_periodic_task_enabled_check = (By.ID, "id_enabled")
    add_periodic_task_drop_down = (By.ID, "id_regtask")
    add_periodic_task_one_off_check = (By.ID, "id_one_off")
    add_periodic_task_argument_field = (By.ID, "id_args")
    add_periodic_task_expire_date_today = (By.XPATH, "//div[@class='form-row field-expires']//div//span[1]//a[1]")
    add_periodic_task_expire_time_field = (By.ID, "id_expires_1")
    add_periodic_task_interval_drop_down = (By.ID, "id_interval")
    add_periodic_task_start_date_today = (By.XPATH, "//div[4]//div[1]//p[1]//span[1]//a[1]")
    add_periodic_task_start_time_today = (By.XPATH, "//div[4]//div[1]//p[1]//span[2]//a[1]")

    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_periodic_task_page(self):
        self._web_driver.verify_text(self.add_periodic_task_title_text, "Add periodic task")

    def verify_change_periodic_task_page(self):
        self._web_driver.verify_text(self.add_periodic_task_change_periodic_task_title_text, "Change periodic task")

    def create_new_periodic_task(self, periodic_task_name, is_enabled):
        self._web_driver.send_value(self.add_periodic_task_name_field, periodic_task_name)
        is_checked = self._web_driver.find_element(self.add_periodic_task_enabled_check).is_selected()
        if not is_checked and is_enabled:
            self._web_driver.click_element(self.add_periodic_task_enabled_check)
        elif is_checked and not is_enabled:
            self._web_driver.click_element(self.add_periodic_task_enabled_check)
        self._web_driver.select_value_from_options(self.add_periodic_task_drop_down,
                                                   "noble.usage_limits.tasks.create_and_send_licensing_report")
        self._web_driver.select_value_from_options(self.add_periodic_task_interval_drop_down, "every minute")
        self._web_driver.send_value(self.add_periodic_task_argument_field, "[2,2020]")
        self._web_driver.click_element(self.add_periodic_task_one_off_check)
        self._web_driver.click_element(self.add_periodic_task_save_button)

    def update_start_end_time_and_enable(self, is_enabled):
        is_checked = self._web_driver.find_element(self.add_periodic_task_enabled_check).is_selected()
        if not is_checked and is_enabled:
            self._web_driver.click_element(self.add_periodic_task_enabled_check)
        elif is_checked and not is_enabled:
            self._web_driver.click_element(self.add_periodic_task_enabled_check)
        self._web_driver.send_value(self.add_periodic_task_argument_field, "[3,2020]")
        self._web_driver.click_element(self.add_periodic_task_start_date_today)
        self._web_driver.click_element(self.add_periodic_task_start_time_today)
        self._web_driver.click_element(self.add_periodic_task_expire_date_today)
        self._web_driver.send_value(self.add_periodic_task_expire_time_field, get_future_time(30))
        self._web_driver.click_element(self.add_periodic_task_save_button)

    def delete_periodic_task(self):
        self._web_driver.click_element(self.add_periodic_task_delete_button)
        self._web_driver.click_element(self.confirm_delete)
