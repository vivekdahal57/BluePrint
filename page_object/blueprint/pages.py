from page_object.global_objects import *
from page_object.blueprint.locators import BlueprintLoginPageLocator, BlueprintDashboardPageLocator

blueprint_login_locator = BlueprintLoginPageLocator()
blueprint_dashboard_locator = BlueprintDashboardPageLocator()


class BlueprintLoginPage(BasePage):

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_page(self):
        self._web_driver.find_element(blueprint_login_locator.username_field)

    def login(self, username, password):
        if username != '' and password != '':
            self._web_driver.send_value(blueprint_login_locator.username_field, username)
            self._web_driver.send_value(blueprint_login_locator.password_field, password)
        self._web_driver.click_element(blueprint_login_locator.sign_in_button)

    def verify_login_fail(self):
        self._web_driver.verify_text(blueprint_login_locator.incorrect_login_message, 'Incorrect email and/or password.')

    def verify_login_pass(self):
        self._web_driver.click_element(blueprint_dashboard_locator.dashboard_blueprint_select_half_button)
        self._web_driver.verify_text(blueprint_dashboard_locator.dashboard_title_text, 'All Collections')


class BlueprintDashboardPage(BasePage):
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj
        self.blueprint_login_page = BlueprintLoginPage(obj)

    def logout(self):
        self._web_driver.wait_until_element_disappear(blueprint_dashboard_locator.loading_text)
        self._web_driver.scroll_to(blueprint_dashboard_locator.profile_drop_down)
        self._web_driver.click_element(blueprint_dashboard_locator.logout_link)
        self.blueprint_login_page.verify_login_page()