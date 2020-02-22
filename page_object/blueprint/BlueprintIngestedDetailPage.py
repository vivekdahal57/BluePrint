from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintIngestedDetailPage(BasePage):
    ingested_collection_name_back_button = (By.XPATH, "//button[@class='title']")
    ingested_document_title_text = (By.XPATH, "//h3[@id='cluster-detail-name']")
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_ingested_document_page(self):
        self._web_driver.scroll_to(self.ingested_document_title_text)
        self._web_driver.verify_text(self.ingested_document_title_text, "Ingested Documents")
