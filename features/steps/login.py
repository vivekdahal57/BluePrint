from behave import given, when, then, step
from page_object.global_objects import blueprint_login_page, blueprint_dashboard_page, admin_login_page, \
    admin_dashboard_page, architect_dashboard_page


def get_username(context, username):
    if username == 'admin_username':
        return context.config.userdata.get('correct_admin_username')
    if username == 'correct_username':
        return context.config.userdata.get('correct_normal_username')
    if username == 'created_username':
        return context.config.userdata.get('created_normal_username')
    if username == 'staff_username':
        return context.config.userdata.get('created_staff_username')
    else:
        return username


def get_password(context, password):
    if password == 'admin_password':
        return context.config.userdata.get('correct_admin_password')
    if password == 'correct_password':
        return context.config.userdata.get('correct_normal_password')
    if password == 'created_password':
        return context.config.userdata.get('created_normal_password')
    if password == 'staff_password':
        return context.config.userdata.get('created_staff_password')
    else:
        return password


@given('user is in blueprint Login page')
def open_browser(context):
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
    blueprint_login_page.verify_login_page()


@step('user reapply blueprint url with http')
def open_browser(context):
    blueprint_login_page.open("http://" + str(context.config.userdata.get('blueprint_url')).split("@")[1])
    blueprint_login_page.verify_login_page()


@step('url changes to https automatically')
def get_url(context):
    url = context.web.get_current_url()
    if "https" not in url:
        assert False, url + " has Error!! No https found!!"


@when('user use {username} and {password}')
def login_attempt(context, username, password):
    if username != 'Blank' and password != 'Blank':
        username = get_username(context, username)
        password = get_password(context, password)
    else:
        username = ''
        password = ''
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
    username = get_username(context, username)
    password = get_password(context, password)
    admin_login_page.login(username, password)


@then('admin user failed to login')
def failed_login(context):
    admin_login_page.verify_login_fail()


@then('normal user {username} failed to authorized')
def failed_login(context, username):
    username = get_username(context, username)
    admin_login_page.verify_authorization_fail(username)


@then('admin user succeed to login')
def pass_login(context):
    admin_dashboard_page.verify_login_pass()


@step('admin user succeed to logout')
def pass_login(context):
    admin_dashboard_page.logout()


@step('user navigate to Architect application')
def user_navigate_to_architect(context):
    blueprint_dashboard_page.navigate_to_architect()
    architect_dashboard_page.verify_architect_dashboard()


@step('user navigate to User Manual page')
def user_navigate_to_user_manual(context):
    blueprint_dashboard_page.navigate_to_user_manual()


@step('user navigate to FAQ page')
def user_navigate_to_faq(context):
    blueprint_dashboard_page.navigate_to_faq()


@step('user navigate to Terms of Service page')
def user_navigate_to_terms_service(context):
    blueprint_dashboard_page.navigate_to_terms_of_service()


@step('user navigate to Google Analytics page')
def user_navigate_to_google_analytics(context):
    blueprint_dashboard_page.navigate_to_terms_of_service()
    blueprint_dashboard_page.navigate_to_google_analytics()
    blueprint_login_page.open(context.config.userdata.get('blueprint_url'))
