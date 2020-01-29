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


class AdminUserListPageLocator:
    user_title_text = (By.XPATH, "//h1[contains(text(),'Select user to change')]")
    user_add_button = (By.XPATH, "//a[@class='addlink']")
    user_change_success = (By.CSS_SELECTOR, "li.success")
    user_search_field = (By.ID, "searchbar")
    user_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    user_search_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")

    def __init__(self):
        pass


class AdminAddUserPageLocator:
    add_user_title_text = (By.XPATH, "//h1[contains(text(),'Add user')]")
    add_user_change_user_title_text = (By.XPATH, "//h1[contains(text(),'Change user')]")
    add_user_username_field = (By.ID, "id_username")
    add_user_password1_field = (By.ID, "id_password1")
    add_user_password2_field = (By.ID, "id_password2")
    add_user_save_button = (By.NAME, "_save")
    add_user_first_name_field = (By.ID, "id_first_name")
    add_user_last_name_field = (By.ID, "id_last_name")
    add_user_email_field = (By.ID, "id_email")
    add_user_active_check = (By.ID, "id_is_active")
    add_user_staff_check = (By.ID, "id_is_staff")
    add_user_super_user_check = (By.ID, "id_is_superuser")
    add_user_groups_from_list = (By.ID, "id_groups_from")
    add_user_group_add_arrow_button = (By.ID, "id_groups_add_link")
    add_user_group_remove_arrow_button = (By.ID, "id_groups_remove_link")
    add_user_groups_to_list = (By.ID, "id_groups_to")
    add_user_group_search_text = (By.ID, "id_groups_input")
    add_user_group_option = (By.XPATH, "//*[@name='groups_old']/option[1]")
    add_user_permission_from_list = (By.ID, "id_user_permissions_from")
    add_user_permission_to_list = (By.ID, "id_user_permissions_to")
    add_user_permission_add_arrow_button = (By.ID, "id_groups_add_link")
    add_user_permission_remove_arrow_button = (By.ID, "id_groups_remove_link")
    add_user_permission_search_text = (By.ID, "id_permissions_input")
    add_user_permission_option = (By.XPATH, "//*[@name='user_permissions_old']/option[1]")
    add_user_delete_button = (By.XPATH, "//a[@class='deletelink']")
    confirm_delete = (By.XPATH, "//form/div[1]/input[2]")

    def __init__(self):
        pass


class AdminUserProfileLocator:
    user_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    user_profile_add_profile_button = (By.XPATH, "//*[@id='content-main']/ul/li[1]/a")
    user_profile_search_field = (By.ID, "searchbar")
    user_profile_search_button = (By.XPATH, "//*[@id='changelist-search']/div/input[2]")
    user_profile_output = (By.XPATH, "//table[@id='result_list']/tbody/tr[1]/th[1]/a")
    user_profile_change_success = (By.XPATH, "//li[@class='success']")

    def __init__(self):
        pass


class AdminAddUserProfileLocator:
    add_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    add_profile_change_profile_title_text = (By.XPATH, "//*[@id='content']/h1")
    add_profile_company_field = (By.ID, "id_company")
    add_profile_image_browse = (By.ID, "id_picture")
    add_profile_users_dropdown = (By.ID, "id_user")
    add_profile_agreed_tos_check = (By.ID, "id_agreed_terms_of_service")
    add_profile_blueprint_tour_check = (By.ID, "id_has_toured_blueprint")
    add_profile_reactor_tour_check = (By.ID, "id_has_toured_reactor")
    add_profile_multiple_login_check = (By.ID, "id_allow_multiple_login")
    add_profile_save_button = (By.NAME, "_save")
    add_profile_delete_button = (By.XPATH, "//a[@class='deletelink']")

    @staticmethod
    def select_user(username):
        return "//*[@id='id_user']/option[contains(text(),'" + username + "')]"

    def __init__(self):
        pass
