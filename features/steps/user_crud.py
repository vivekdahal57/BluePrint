from behave import given, when, then, step
from page_object.global_objects import *


@given("admin user is in dashboard page after login with {username} and {password}")
def login(context, username, password):
    admin_login_page.open(context.config.userdata.get('blueprint_url') + '/admin')
    admin_login_page.verify_login_page()
    admin_login_page.login(username, password)
    admin_dashboard_page.verify_login_pass()


@when("admin user creates a user with username {username} and password {password}")
def create_user(context, username, password):
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.verify_users_list_page()
    admin_user_list_page.goto_add_user_page()
    admin_add_user_page.verify_add_user_page()
    admin_add_user_page.create_user(username, password)
    admin_add_user_page.change_user("Automation", "User1", "test@test.com", True, False, False, ['Test Group'], "")
    admin_user_list_page.verify_users_list_page()
    time.sleep(2)
    # admin_user_list_page.verify_user_change_success(username)
    admin_dashboard_page.logout()


@then("user with username {username} and password {password} is able to login and logout")
def login_with_new_user(context, username, password):
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()
    blueprint_login_page.login(username, password)
    blueprint_dashboard_page.skip_tour(True)
    blueprint_login_page.verify_login_pass()
    blueprint_dashboard_page.logout()


@step("admin user can delete {username} user")
def login_with_new_user(context, username):
    admin_dashboard_page.goto_users_list()
    admin_user_list_page.search_and_land_to_change_user(username)
    admin_add_user_page.verify_change_user_page()
    admin_add_user_page.delete_user()
    admin_user_list_page.verify_users_list_page()
    admin_dashboard_page.logout()


@then("deleted user with username {username} and password {password} cannot login")
def login_with_new_user(context, username, password):
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()
    blueprint_login_page.login(username, password)
    blueprint_login_page.verify_login_fail()


@when("admin user creates a user profile with username {username}")
def create_user_profile(context, username):
    admin_dashboard_page.goto_users_profile_list()
    admin_user_profile_page.verify_user_profile_page()
    admin_user_profile_page.goto_add_user_profile_page()
    admin_add_user_profile_page.verify_add_user_profile_page()
    admin_add_user_profile_page.add_user_profile("AutomationCompany", username,
                                                 "",
                                                 False, False, False, False)
    admin_user_profile_page.verify_user_profile_page()
    admin_dashboard_page.logout()
