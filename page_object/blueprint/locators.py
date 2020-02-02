# oop in python
from selenium.webdriver.common.by import By


class BlueprintLoginPageLocator:
    sign_in_button = (By.XPATH, '//button[@class=\'button button--primary button--min-width mt-31 w-100\']')
    login_title_text = (By.XPATH, '//div[@class=\'modal-form\']')
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    reset_password_link = (By.LINK_TEXT, 'Reset Password')
    incorrect_login_message = (By.XPATH, '/html[1]/body[1]/aside[1]/div[1]/div[2]/p[1]')

    def __init__(self):
        pass


class BlueprintDashboardPageLocator:
    dashboard_title_text = (By.XPATH, "//h2[contains(text(),'All Collections')]")
    dashboard_blueprint_select_half_button = (By.XPATH,
                                              "//div[@class='app-selector__action app-selector__action--blueprint']//button[@class='button button--primary button--min-width app-selector__cta']")
    profile_drop_down = (By.XPATH, "//div[@class='profile']/div[1]")
    logout_link = (By.XPATH, "//span[contains(text(),'Logout')]")
    loading_text = (By.XPATH, "//p[contains(text(),'Loading...')]")
    tos_skip_tour_link = (By.XPATH, "//span[contains(text(),'Skip Tour')]")
    tos_i_agree = (By.XPATH, "//div[@class='form-checkbox__view']")
    tos_agree_continue = (By.XPATH, "//span[contains(text(),'Agree and Continue')]")
    tos_get_started = (By.XPATH, "//span[contains(text(),'Get Started')]")
    dashboard_left_menu_drop_down = (By.XPATH, "//div[@class='left-side']")
    dashboard_left_new_col_button = (By.XPATH, "//span[contains(text(),'+ New Collection')]")
    dashboard_browse_file_button = (By.XPATH, "//button[@class='upload-content']")

    def __init__(self):
        pass


class BlueprintCollectionDetailLocator:
    dashboard_collection_name_popup = (By.XPATH, "//input[@class='textInput']")
    dashboard_collection_ok_button = (By.XPATH, "//div[@class='modal-form__actions']//button[@class='button button--primary button--min-width']")
    dashboard_collection_name_text = (By.ID, "collection-header-name")

    def __init__(self):
        pass
