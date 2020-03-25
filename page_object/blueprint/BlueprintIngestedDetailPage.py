from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from page_object.blueprint.BlueprintLoginPage import BlueprintLoginPage


class BlueprintIngestedDetailPage(BasePage):
    ingested_collection_name_back_button = (By.XPATH, "//button[@class='title']")
    ingested_document_title_text = (By.XPATH, "//h3[@id='cluster-detail-name']")
    ingested_routing_tab = (By.XPATH, "//li[contains(text(),'Routing')]")
    ingested_new_doc_type_tab = (By.XPATH, "//li[contains(text(),'New Doc. Type Identified')]")
    ingested_exceptions_tab = (By.XPATH, "//li[contains(text(),'Exceptions')]")
    ingested_file_path = "//div[@data-clientfile-id]//div[1]//div[1]//div[1]//div"
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def verify_ingested_document_page(self):
        self._web_driver.scroll_to(self.ingested_document_title_text)
        self._web_driver.verify_text(self.ingested_document_title_text, "Ingested Documents")

    def ingested_files_in_given_tab(self, tab_name, file_list):
        error = False
        error_list = []
        if tab_name.lower() == 'routing':
            self._web_driver.click_element(self.ingested_routing_tab)
        elif tab_name.lower() == 'exceptions':
            self._web_driver.click_element(self.ingested_exceptions_tab)
        else:
            self._web_driver.click_element(self.ingested_new_doc_type_tab)
        element_count = 0
        try:
            element_count = len(self._web_driver.find_elements((By.XPATH, self.ingested_file_path), 2))
            if element_count == 0 and file_list == []:
                raise TimeoutException()
            elif element_count > 0 and file_list == []:
                raise ValueError("Files found in " + tab_name + " Tab.")
            else:
                for file in file_list:
                    try:
                        self._web_driver.find_element(
                            (By.XPATH, self.ingested_file_path + "[contains(text(),'" + file + "')]"),
                            2)
                    except TimeoutException:
                        error = True
                        error_list.append(file)
                if error:
                    raise ValueError('Given file or files ' + (','.join(error_list)) + ' is not visible')
        except TimeoutException:
            print(str(element_count) + " Files found")
