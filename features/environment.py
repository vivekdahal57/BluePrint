import os
import allure
from behave import use_fixture
from behave.log_capture import capture
from page_object.driver_factory_fixture import browser_chrome, browser_firefox, browser_ie, base_page,\
    browser_chrome_headless, browser_firefox_headless

# before tag is used when there is need of executing tests in a given fixture
# def before_tag(context, tag):
#     if tag == "fixture.browser.chrome":
#         use_fixture(browser_chrome, context)
#     if tag == "fixture.browser.firefox":
#         use_fixture(browser_firefox, context)
#     if tag == "fixture.browser.ie":
#         use_fixture(browser_ie, context)

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
        # scenario_error_dir = os.path.join(directory + '/', 'feature_error')
        # make_dir(scenario_error_dir)
        # scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
        #                                   + '_' + time.strftime("%H%M%S_%d_%m_%Y")
        #                                   + '.png')
        # base_page.driver.save_screenshot(scenario_file_path)


def make_dir(directories):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(directories):
        os.makedirs(directories)
