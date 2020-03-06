import time

from behave import given, when, then, step
from page_object.global_objects import blueprint_login_page, blueprint_dashboard_page, admin_login_page, \
    admin_dashboard_page, blueprint_collection_details_page, architect_dashboard_page


@given('user is in blueprint Login page')
def open_browser(context):
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()


@when('user use {username} and {password}')
def login_attempt(context, username, password):
    blueprint_login_page.login(username, password)


@then('user failed to login')
def failed_login(context):
    blueprint_login_page.verify_login_fail()


@then('user succeed to login')
def pass_login(context):
    blueprint_dashboard_page.verify_login_pass()


@then('user succeed to logout')
def pass_login(context):
    blueprint_dashboard_page.logout()


@step('user is in admin Login page')
def open_browser(context):
    admin_login_page.open(context.config.userdata.get('blueprint_url') + '/admin')
    admin_login_page.verify_login_page()


@when('admin user use {username} and {password}')
def login_attempt(context, username, password):
    admin_login_page.login(username, password)


@then('admin user failed to login')
def failed_login(context):
    admin_login_page.verify_login_fail()


@then('normal user {username} failed to authorized')
def failed_login(context, username):
    admin_login_page.verify_authorization_fail(username)


@then('admin user succeed to login')
def pass_login(context):
    admin_dashboard_page.verify_login_pass()


@step('admin user succeed to logout')
def pass_login(context):
    admin_dashboard_page.logout()


@step('logged in user can create collection with name {collection_name} and with file {file_name}')
def create_collection(context, collection_name, file_name):
    blueprint_dashboard_page.add_new_collection(context.config.userdata.get('upload_file_location') + file_name,
                                                collection_name)
    blueprint_collection_details_page.verify_collection_details_page(collection_name)


@step('user navigate to Architect application')
def user_navigate_to_architect(context):
    blueprint_dashboard_page.navigate_to_architect()
    architect_dashboard_page.verify_architect_dashboard()
