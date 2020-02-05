from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class BlueprintLoginPage(BasePage):
    sign_in_button = (By.XPATH, '//button[@class=\'button button--primary button--min-width mt-31 w-100\']')
    login_title_text = (By.XPATH, '//div[@class=\'modal-form\']')
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    reset_password_link = (By.LINK_TEXT, 'Reset Password')
    incorrect_login_message = (By.XPATH, '/html[1]/body[1]/aside[1]/div[1]/div[2]/p[1]')

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_page(self):
        self._web_driver.find_element(self.username_field)

    def login(self, username, password):
        if username != '' and password != '':
            self._web_driver.send_value(self.username_field, username)
            self._web_driver.send_value(self.password_field, password)
        self._web_driver.click_element(self.sign_in_button)

    def verify_login_fail(self):
        self._web_driver.verify_text(self.incorrect_login_message, 'Incorrect email and/or password.')
