from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintClusterDetailPage(BasePage):
    cluster_detail_title_text = (By.ID, "cluster-detail-name")

    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_cluster_details_page(self, cluster_name):
        self._web_driver.scroll_to(self.cluster_detail_title_text)
        self._web_driver.verify_text(self.cluster_detail_title_text, cluster_name)
