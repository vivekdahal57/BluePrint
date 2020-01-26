from behave import given, when, then
from page_object.global_objects import blueprint_login_page, blueprint_dashboard_page, admin_login_page, \
    admin_dashboard_page


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
    blueprint_login_page.verify_login_pass()


@then('user succeed to logout')
def pass_login(context):
    blueprint_dashboard_page.logout()


@given('user is in admin Login page')
def open_browser(context):
    admin_login_page.open(context.config.userdata.get('blueprint_url') + '/admin')
    admin_login_page.verify_login_page()


@when('admin user use {username} and {password}')
def login_attempt(context, username, password):
    admin_login_page.login(username, password)


@then('admin user failed to login')
def failed_login(context):
    admin_login_page.verify_login_fail()


@then('admin user succeed to login')
def pass_login(context):
    admin_dashboard_page.verify_login_pass()


@then('admin user succeed to logout')
def pass_login(context):
    admin_dashboard_page.logout()
