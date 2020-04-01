import time

from behave import given, when, then, step
from page_object.global_objects import *
from features.steps.login import get_password, get_username


@given("admin user is in dashboard page after login with {username} and {password}")
def login(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    admin_login_page.open(context.config.userdata.get('blueprint_url') + '/admin')
    admin_login_page.verify_login_page()
    admin_login_page.login(username, password)
    admin_dashboard_page.verify_login_pass()


@when("admin user creates a inactive user with username {username} and password {password}")
def create_user(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    is_staff = False
    if 'staff' in username:
        is_staff = True
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.verify_users_list_page()
    admin_user_list_page.goto_add_user_page()
    admin_add_user_page.verify_add_user_page()
    admin_add_user_page.create_user(username, password)
    admin_add_user_page.change_user("Automation", "User1", "test@test.com", False, is_staff, False,
                                    ['System Administrators'], "")
    admin_user_list_page.verify_users_list_page()
    time.sleep(1)
    # admin_user_list_page.verify_user_change_success(username)


@when("admin user changes a inactive user to active with username {username}")
def update_user(context, username):
    username = get_username(context, username)
    is_staff = False
    if 'staff' in username:
        is_staff = True
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.verify_users_list_page()
    admin_user_list_page.search_and_land_to_change_user(username)
    admin_add_user_page.verify_change_user_page()
    admin_add_user_page.change_user("Automation", "User1", "test@test.com", True, is_staff, False,
                                    [''], "")
    admin_user_list_page.verify_users_list_page()
    time.sleep(1)


@then("user with username {username} and password {password} is able to login")
def login_with_new_user(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()
    blueprint_login_page.login(username, password)
    blueprint_dashboard_page.skip_tour(True)
    blueprint_dashboard_page.verify_login_pass()


@then("inactive user with username {username} and password {password} is not able to login")
def login_with_new_user(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()
    blueprint_login_page.login(username, password)
    blueprint_login_page.verify_login_fail()


@step("admin user can delete {username} user")
def login_with_new_user(context, username):
    username = get_username(context, username)
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.search_and_land_to_change_user(username)
    admin_add_user_page.verify_change_user_page()
    admin_add_user_page.delete_user()
    admin_user_list_page.verify_users_list_page()


@then("deleted user with username {username} and password {password} cannot login")
def login_with_new_user(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()
    blueprint_login_page.login(username, password)
    blueprint_login_page.verify_login_fail()


@when("admin user creates a user profile with username {username}")
def create_user_profile(context, username):
    username = get_username(context, username)
    admin_dashboard_page.goto_users_profile_list()
    admin_user_profile_page.verify_user_profile_page()
    admin_user_profile_page.goto_add_user_profile_page()
    admin_add_user_profile_page.verify_add_user_profile_page()
    admin_add_user_profile_page.add_user_profile("AutomationCompany", username, "", False, False, False, False)
    admin_user_profile_page.verify_user_profile_page()
