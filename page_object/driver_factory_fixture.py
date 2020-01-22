from behave import fixture
from seleniumwire import webdriver
# from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from page_object.pages import BasePage, BlueprintLoginPage
import os

base_page = BasePage(None)
login_page = BlueprintLoginPage(base_page)

directory = os.path.dirname(os.path.dirname(__file__))


# yield is used to quit the browser when default timeout period is ended and test is still not passing
def browser_chrome(context):
    browser = webdriver.Chrome(os.path.join(directory + '/', 'resource/chromedriver.exe'))
    val = dict({'authorization': 'Basic bm9ibGVfdGVhbTppdCB3YXMgdGhlIGJsdXJzdCBvZiB0aW1lcw=='})
    browser.header_overrides = val
    context.web = BasePage(browser)
    yield context.web
    browser.quit()


def browser_chrome_headless(context):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=1600x900")
    browser = webdriver.Chrome(os.path.join(directory + '/', 'resource/chromedriver.exe'),
                               chrome_options=chrome_options)
    context.web = BasePage(browser)
    yield context.web
    browser.quit()


def browser_ie(context):
    browser = webdriver.Ie(os.path.join(directory + '/', 'resource/IEDriverServer.exe'))
    context.web = BasePage(browser)
    yield context.web
    browser.quit()


def browser_firefox(context):
    # for firefox browser, gecko driver path is kept in the environment's PATH variable
    browser = webdriver.Firefox()
    context.web = BasePage(browser)
    yield context.web
    browser.quit()


def browser_firefox_headless(context):
    # for firefox browser, gecko driver path is kept in the environment's PATH variable
    firefox_options = Options()
    firefox_options.headless = True
    firefox_options.add_argument("--window-size=1600x900")
    firefox_options.add_argument('--disable-gpu')
    browser = webdriver.Firefox(firefox_options=firefox_options)
    context.web = BasePage(browser)
    yield context.web
    browser.quit()
