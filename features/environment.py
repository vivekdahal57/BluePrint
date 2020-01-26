import os
import allure
from behave import use_fixture
from behave.log_capture import capture
from page_object.driver_factory_fixture import browser_chrome, browser_firefox, browser_ie, base_page, \
    browser_chrome_headless, browser_firefox_headless

""" 
before all is called in order to execute before any tests starts executing
its parameters can ve either provided in ini file or from the command line
"""


def before_all(context):
    if context.config.userdata.get('browser') == "chrome":
        if context.config.userdata.get('headless').lower() == "true":
            use_fixture(browser_chrome_headless, context)
        use_fixture(browser_chrome, context)
    if context.config.userdata.get('browser') == "firefox":
        if context.config.userdata.get('headless').lower() == "true":
            use_fixture(browser_firefox_headless, context)
        use_fixture(browser_firefox, context)
    if context.config.userdata.get('browser') == "ie":
        use_fixture(browser_ie, context)


@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        allure.attach(base_page.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


def make_dir(directories):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(directories):
        os.makedirs(directories)
