# oop in python
from selenium.webdriver.common.by import By


class SearchPageLocator:
    search_element = (By.NAME, 'q')

    def __init__(self):
        pass


class HomePageLocator:
    sign_in_link = (By.XPATH, '//a[@class=\'HeaderMenu-link no-underline mr-3\']')
    home_title_text = (By.XPATH, '//h1[@class=\'h000-mktg text-white lh-condensed-ultra mb-3\']')

    def __init__(self):
        pass


class LoginPageLocator:
    sign_in_button = (By.XPATH, '//button[@class=\'button button--primary button--min-width mt-31 w-100\']')
    login_title_text = (By.XPATH, '//div[@class=\'modal-form\']')
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    reset_password_link = (By.LINK_TEXT, 'Reset Password')
    incorrect_login_message = (By.XPATH, '/html[1]/body[1]/aside[1]/div[1]/div[2]/p[1]')

    def __init__(self):
        pass


class DashboardPageLocator:
    dashboard_title_text = (By.XPATH, '//h2[contains(text(),\'All Collections\')]')
    dashboard_blueprint_select_half_button = (By.XPATH, '//div[@class=\'app-selector__action app-selector__action--blueprint\']//button[@class=\'button button--primary button--min-width app-selector__cta\']')

    def __init__(self):
        pass
