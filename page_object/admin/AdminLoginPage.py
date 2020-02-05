from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AdminLoginPage(BasePage):
    sign_in_button = (By.XPATH, '//div[@class=\'submit-row\']//input')
    login_title_text = (By.XPATH, '//a[contains(text(),\'Django administration\')]')
    username_field = (By.ID, 'id_username')
    password_field = (By.ID, 'id_password')
    incorrect_login_message = (By.XPATH, "//p[@class='errornote']")

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
        self._web_driver.verify_text(self.incorrect_login_message,
                                     'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')

    def verify_authorization_fail(self, username):
        self._web_driver.verify_text(self.incorrect_login_message,
                                     'You are authenticated as ' + username + ', but are not authorized to access this page. Would you like to login to a different account?')
