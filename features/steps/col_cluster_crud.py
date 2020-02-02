from behave import step
from page_object.global_objects import *


@step("admin user can delete {collection_name} collection")
def login_with_new_user(context, collection_name):
    admin_dashboard_page.goto_collection_list()
    admin_collection_list_page.search_and_land_to_change_collection(collection_name)
    admin_add_collection_page.verify_change_collection_page()
    admin_add_collection_page.delete_collection()
    admin_collection_list_page.verify_collections_list_page()
    admin_dashboard_page.logout()
