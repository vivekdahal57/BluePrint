from page_object.global_objects import *
from page_object.admin.locators2 import AdminCollectionsListPageLocator, AdminAddCollectionPageLocator, \
    AdminClusterListPageLocator, AdminAddClusterPageLocator

admin_collections_list_locator = AdminCollectionsListPageLocator()
admin_add_collection_locator = AdminAddCollectionPageLocator()
admin_cluster_list_locator = AdminClusterListPageLocator
admin_add_cluster_locator = AdminAddClusterPageLocator()


class AdminCollectionsListPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_collections_list_page(self):
        self._web_driver.verify_text(admin_collections_list_locator.collection_title_text,
                                     "Select collection to change")

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
        self._web_driver.verify_text(admin_add_collection_locator.add_collection_change_collection_title_text,
                                     "Change collection")

    def delete_collection(self):
        self._web_driver.click_element(admin_add_collection_locator.add_collection_delete_button)
        self._web_driver.click_element(admin_add_collection_locator.confirm_delete)


class AdminClusterListPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_cluster_list_page(self):
        self._web_driver.verify_text(admin_cluster_list_locator.cluster_title_text,
                                     "Select cluster to change")

    def goto_add_cluster_page(self):
        self._web_driver.scroll_to(admin_cluster_list_locator.cluster_add_button)
        self._web_driver.click_element(admin_cluster_list_locator.cluster_add_button)

    def search_and_land_to_change_cluster(self, cluster_name):
        self._web_driver.send_value(admin_cluster_list_locator.cluster_search_field, cluster_name)
        self._web_driver.click_element(admin_cluster_list_locator.cluster_search_button)
        self._web_driver.verify_text(admin_cluster_list_locator.cluster_search_output, cluster_name)
        self._web_driver.click_element(admin_cluster_list_locator.cluster_search_output)


class AdminAddClusterPage(BasePage):
    def __init__(self, obj):
        self._web_driver = obj

    def verify_add_cluster_page(self):
        self._web_driver.verify_text(admin_add_cluster_locator.add_cluster_title_text, "Add cluster")

    def verify_change_cluster_page(self):
        self._web_driver.verify_text(admin_add_cluster_locator.add_cluster_change_cluster_title_text,
                                     "Change cluster")

    def create_or_change_cluster(self, cluster_name, collection_name, status):
        self._web_driver.send_value(admin_add_cluster_locator.add_cluster_name_field, cluster_name)
        self._web_driver.select_value_from_options(admin_add_cluster_locator.add_cluster_status_select, status)
        self._web_driver.select_value_by_partial_text_options(
            admin_add_cluster_locator.add_cluster_collection_select_id, collection_name)
        self._web_driver.click_element(admin_add_cluster_locator.add_cluster_save_button)

    def delete_cluster(self):
        self._web_driver.click_element(admin_add_cluster_locator.add_cluster_delete_button)
        self._web_driver.click_element(admin_add_cluster_locator.confirm_delete)
