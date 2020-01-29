from behave import given, when
from page_object.global_objects import *


# Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
#       When admin user creates a user with username automation_user1 and password Password#1
#       Then user with username automation_user1 and password Password#1 is able to login
#       Then admin user can delete user with username automation_user1
#       Then deleted user with username automation_user1 and password Password#1 cannot login
@given("admin user is in dashboard page after login with {username} and {password}")
def login(context, username, password):
    admin_login_page.open(context.config.userdata.get('blueprint_url') + '/admin')
    admin_login_page.verify_login_page()
    admin_login_page.login(username, password)
    admin_dashboard_page.verify_login_pass()


@when("admin user creates a user with username {username} and password {password}")
def create_user(context, username, password):
    admin_dashboard_page.create
