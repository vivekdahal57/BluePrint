import time

from page_object.base_page import BasePage
from page_object.admin.pages import AdminLoginPage, AdminDashboardPage, AdminUsersListPage, AdminAddUserPage, \
    AdminAddUserProfilePage, AdminUserProfileListPage
from page_object.blueprint.pages import BlueprintLoginPage, BlueprintDashboardPage

# all global objects for pages
base_page = BasePage(None)
blueprint_login_page = BlueprintLoginPage(base_page)
blueprint_dashboard_page = BlueprintDashboardPage(base_page)
admin_login_page = AdminLoginPage(base_page)
admin_dashboard_page = AdminDashboardPage(base_page)
admin_user_list_page = AdminUsersListPage(base_page)
admin_add_user_page = AdminAddUserPage(base_page)
admin_user_profile_page = AdminUserProfileListPage(base_page)
admin_add_user_profile_page = AdminAddUserProfilePage(base_page)

