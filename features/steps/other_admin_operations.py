import time
from behave import step
from page_object.global_objects import *


@step("admin user can create a periodic task with name {task_name} and enable {is_enabled} status")
def create_user(context, task_name, is_enabled):
    admin_dashboard_page.goto_periodic_tasks_list()
    admin_periodic_task_list_page.verify_periodic_task_list_page()
    admin_periodic_task_list_page.goto_add_periodic_task_page()
    admin_add_periodic_task_page.verify_add_periodic_task_page()
    admin_add_periodic_task_page.create_new_periodic_task(task_name, is_enabled)
    admin_periodic_task_list_page.verify_periodic_task_list_page()
    time.sleep(1)


@step("admin user can run the periodic task {task_name} from list page")
def login_with_new_user(context, task_name):
    admin_dashboard_page.go_to_dashboard_page()
    admin_dashboard_page.goto_periodic_tasks_list()
    admin_periodic_task_list_page.verify_periodic_task_list_page()
    admin_periodic_task_list_page.search_and_run_periodic_task(task_name)


@step("admin user can enable {is_enabled} to {task_name} periodic task with start end datetime")
def login_with_new_user(context, task_name, is_enabled):
    admin_dashboard_page.goto_periodic_tasks_list()
    admin_periodic_task_list_page.verify_periodic_task_list_page()
    admin_periodic_task_list_page.search_and_land_to_change_periodic_task(task_name)
    admin_add_periodic_task_page.update_start_end_time_and_enable(is_enabled)


@step("admin user can delete {task_name} periodic task")
def login_with_new_user(context, task_name):
    admin_dashboard_page.goto_periodic_tasks_list()
    admin_periodic_task_list_page.verify_periodic_task_list_page()
    admin_periodic_task_list_page.search_and_land_to_change_periodic_task(task_name)
    admin_add_periodic_task_page.verify_change_periodic_task_page()
    admin_add_periodic_task_page.delete_periodic_task()
    admin_periodic_task_list_page.verify_periodic_task_list_page()
