from page_object.global_objects import *
from page_object.admin.locators2 import AdminCollectionsListPageLocator, AdminAddCollectionPageLocator

admin_collections_list_locator = AdminCollectionsListPageLocator()
admin_add_collection_locator = AdminAddCollectionPageLocator()


class AdminCollectionsListPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_collections_list_page(self):
        self._web_driver.verify_text(admin_collections_list_locator.collection_title_text, "Select collection to change")

    def goto_add_collection_page(self):
        self._web_driver.scroll_to(admin_collections_list_locator.collection_add_button)
        self._web_driver.click_element(admin_collections_list_locator.collection_add_button)

    def search_and_land_to_change_collection(self, collection_name):
        self._web_driver.send_value(admin_collections_list_locator.collection_search_field, collection_name)
        self._web_driver.click_element(admin_collections_list_locator.collection_search_button)
        self._web_driver.verify_text(admin_collections_list_locator.collection_search_output, collection_name)
        self._web_driver.click_element(admin_collections_list_locator.collection_search_output)


class AdminAddCollectionPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_collection_page(self):
        self._web_driver.verify_text(admin_add_collection_locator.add_collection_title_text, "Add collection")

    def verify_change_collection_page(self):
        self._web_driver.verify_text(admin_add_collection_locator.add_collection_change_collection_title_text, "Change collection")

    def delete_collection(self):
        self._web_driver.click_element(admin_add_collection_locator.add_collection_delete_button)
        self._web_driver.click_element(admin_add_collection_locator.confirm_delete)