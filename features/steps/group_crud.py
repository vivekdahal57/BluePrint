import time

from behave import step

from features.steps.login import get_username
from page_object.global_objects import *


@step("admin user can create a group with name {group_name}")
def create_user(context, group_name):
    admin_dashboard_page.goto_groups_list()
    admin_group_list_page.verify_group_list_page()
    admin_group_list_page.goto_add_group_page()
    admin_add_group_page.verify_add_group_page()
    admin_add_group_page.create_new_group(group_name)
    admin_group_list_page.verify_group_list_page()
    time.sleep(1)


@step("admin user unselect group {group_name} for username {username}")
def unassgin_group_from_user(context, username, group_name):
    username = get_username(context, username)
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.verify_users_list_page()
    admin_user_list_page.search_and_land_to_change_user(username)
    admin_add_user_page.verify_change_user_page()
    admin_add_user_page.unselect_group_and_save(group_name)
    admin_user_list_page.verify_users_list_page()
    admin_dashboard_page.go_to_dashboard_page()
    time.sleep(1)


@step("admin user can assign group {group_name} to username {username}")
def assign_group_to_user(context, username, group_name):
    username = get_username(context, username)
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.verify_users_list_page()
    admin_user_list_page.search_and_land_to_change_user(username)
    admin_add_user_page.verify_change_user_page()
    admin_add_user_page.assign_group_and_save([group_name])
    admin_user_list_page.verify_users_list_page()
    admin_dashboard_page.go_to_dashboard_page()
    time.sleep(1)


@step("admin user can delete {group_name} group")
def login_with_new_user(context, group_name):
    admin_dashboard_page.goto_groups_list()
    admin_group_list_page.search_and_land_to_change_group(group_name)
    admin_add_group_page.verify_change_group_page()
    admin_add_group_page.delete_group()
    admin_group_list_page.verify_group_list_page()


@step("admin user can assign a group with name {group_name} to the collection {collection_name}")
def change_cluster(context, group_name, collection_name):
    admin_dashboard_page.goto_collection_list()
    admin_collection_list_page.verify_collections_list_page()
    admin_collection_list_page.search_and_land_to_change_collection(collection_name)
    admin_add_collection_page.verify_change_collection_page()
    admin_add_collection_page.assign_group_to_collection(group_name)
