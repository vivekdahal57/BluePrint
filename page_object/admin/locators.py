from selenium.webdriver.common.by import By


class AdminLoginPageLocator:
    sign_in_button = (By.XPATH, '//div[@class=\'submit-row\']//input')
    login_title_text = (By.XPATH, '//a[contains(text(),\'Django administration\')]')
    username_field = (By.ID, 'id_username')
    password_field = (By.ID, 'id_password')
    incorrect_login_message = (By.XPATH, "//p[@class='errornote']")

    def __init__(self):
        pass


class AdminDashboardPageLocator:
    dashboard_title_text = (By.XPATH, "//h1[contains(text(),'Site administration')]")
    logout_link = (By.XPATH, "//a[contains(text(),'Log out')]")
    logout_page_title = (By.XPATH, "// h1[contains(text(), 'Logged out')]")
    user_profile_link = (By.XPATH, "//a[contains(text(),'User profiles')]")
    user_link = (By.XPATH, "//a[contains(text(),'Users')]")

    def __init__(self):
        pass


class AdminUserPageLocator:
    user_title_text = (By.XPATH, "//h1[contains(text(),'Select user to change')]")
    user_add_button = (By.XPATH, "//a[@class='addlink']")

    def __init__(self):
        pass


class AdminAddUserPageLocator:
    add_user_title_text = (By.XPATH, "//h1[contains(text(),'Add user')]")
    add_user_username_field = (By.ID, "id_username")
    add_user_password1_field = (By.ID, "id_password1")
    add_user_password2_field = (By.ID, "id_password2")
    add_user_save_button = (By.NAME, "_save")
    add_user_first_name_field = (By.ID, "id_first_name")
    add_user_last_name_field = (By.ID, "id_last_name")
    add_user_email_field= (By.ID, "id_email")
    add_user_id_check = (By.ID, "id_is_active")
    add_user_staff_check = (By.ID, "id_is_staff")
    add_user_super_user_check = (By.ID, "id_is_superuser")
    add_user_groups_from_list = (By.ID, "id_groups_from")
    add_user_groups_to_list = (By.ID, "id_groups_to")
    add_user_permission_from_list = (By.ID, "id_user_permissions_from")
    add_user_permission_to_list = (By.ID, "id_user_permissions_to")
    add_user_delete_button = (By.XPATH, "//a[@class='deletelink']")

    def __init__(self):
        pass
