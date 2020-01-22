from behave import given, when, then
from selenium.webdriver.common.alert import Alert

from page_object.driver_factory_fixture import base_page, login_page


@given('user is in Login page')
def open_browser(context):
    login_page.open(context.config.userdata.get('base_url'))
    login_page.verify_login_page()


@when('user use {username} and {password}')
def login_attempt(context, username, password):
    login_page.login(username, password)


@then('user failed to login')
def failed_login(context):
    login_page.verify_login_fail()


@then('user succeed to login')
def pass_login(context):
    login_page.verify_login_pass()
