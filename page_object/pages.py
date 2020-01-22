import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from page_object.locators import LoginPageLocator, DashboardPageLocator, HomePageLocator

login_locator = LoginPageLocator()
dashboard_locator = DashboardPageLocator()
home_locator = HomePageLocator()


class BasePage(object):
    __TIMEOUT = 30

    class __BasePage:
        def __init__(self, web_driver):
            self.driver = web_driver

        def __str__(self):
            return repr(self) + self.driver

    _web_driver = None

    def __init__(self, web_driver):
        super(BasePage, self).__init__()
        if not BasePage._web_driver:
            BasePage._web_driver = BasePage.__BasePage(web_driver)
        else:
            BasePage._web_driver.driver = web_driver

    def __getattr__(self, web_driver):
        return getattr(self._web_driver, web_driver)

    def open(self, url):
        # This method will type the given url in the browser
        self._web_driver.driver.set_page_load_timeout(30)
        self._web_driver.driver.maximize_window()
        self._web_driver.driver.get(url)

    def find_element_by_xpath(self, xpath):
        # This method finds the element using xpath and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_elements_by_xpath(self, xpath):
        # This method find all the elements using xpath and return the elements
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_element_by_id(self, identity):
        # This method finds the element using id and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.ID, identity)))

    def find_element_by_name(self, name):
        # This method finds the element using name and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_element(self, element):
        # This method wait for the element and return the element
        _web_driver_wait = WebDriverWait(self._web_driver.driver, BasePage.__TIMEOUT)
        return _web_driver_wait.until(EC.visibility_of_element_located(element))

    def get_text(self, element):
        # This method get text from the element and return the text
        elm = self.find_element(element)
        return elm.text

    def verify_text(self, element, text):
        # This method get text from the element and verify it
        assert self.get_text(element) in text, \
            'Element {} not found'.format(element)

    def click_element(self, element):
        # This method clicks on the element provided by the user.
        # It first find the element, wait till its loaded and then click it.
        elm = self.find_element(element)
        elm.click()

    def reload_page(self):
        # It reloads the page
        self._web_driver.driver.refresh(500)

    def close_browser(self):
        # It closes the browser
        self._web_driver.driver.close()

    def send_value(self, element, value):
        # It types the value send by the user in the provided element.
        # It first find the element, wait till its loaded, clears it if
        # Enter or Return is not send and finally type the value.
        elm = self.find_element(element)
        if value != Keys.ENTER and value != Keys.RETURN:
            elm.clear()
        elm.send_keys(value)

    def zoom_browser(self, value):
        # This methods sets the zoom ratio with the provided value
        self._web_driver.driver.execute_script('document.body.style.zoom=\'' + value + '\'')

    def drag_from_drop_to(self, source_element, destination_element):
        # This method drag element from source to destination
        # (sometimes it might not work so scroll down to element first and then drag drop)
        ActionChains(self._web_driver.driver).drag_and_drop(self.find_element(source_element),
                                                            self.find_element(destination_element)).perform()

    def scroll_to(self, element):
        ActionChains(self._web_driver.driver).move_to_element(self.find_element(element)).perform()


class BlueprintDashboardPage(BasePage):
    _web_driver_wait = None

    def __init__(self, obj):
        self._web_driver = obj

    def click_signin_link(self):
        self._web_driver.click_element(home_locator.sign_in_link)

    def verify_home_page(self):
        self._web_driver.verify_text(home_locator.home_title_text, 'Built for developers')


class BlueprintLoginPage(BasePage):

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_page(self):
        self._web_driver.find_element(login_locator.username_field)

    def login(self, username, password):
        if username != '' and password != '':
            self._web_driver.send_value(login_locator.username_field, username)
            self._web_driver.send_value(login_locator.password_field, password)
        self._web_driver.click_element(login_locator.sign_in_button)

    def verify_login_fail(self):
        self._web_driver.verify_text(login_locator.incorrect_login_message, 'Incorrect email and/or password.')

    def verify_login_pass(self):
        self._web_driver.click_element(dashboard_locator.dashboard_blueprint_select_half_button)
        self._web_driver.verify_text(dashboard_locator.dashboard_title_text, 'All Collections')
