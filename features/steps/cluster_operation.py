from behave import step
from page_object.global_objects import *


@step("admin user can delete a cluster with name {cluster_name}")
def delete_cluster(context, cluster_name):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.delete_cluster()
    admin_cluster_list_page.verify_cluster_list_page()


@step("logged in user can search with filename {filename} and land on it")
def search_filename_from_dashboard(context, filename):
    blueprint_dashboard_page.search_and_land(filename)
    blueprint_ingested_document_page.verify_ingested_document_page()


@step(
    "user can search cluster with collection check {col_check_value}, cluster check {cluster_check_value} and valid filename {filename} and land on {cluster_name} page")
def search_file_from_collection(context, filename, col_check_value, cluster_check_value, cluster_name):
    blueprint_cluster_details_page.search_valid_file_and_land(filename, col_check_value, cluster_check_value)
    blueprint_cluster_details_page.verify_cluster_details_page(cluster_name)


@step("user can search cluster with invalid filename {filename}")
def search_text(context, filename):
    blueprint_cluster_details_page.search_invalid_file(filename)


@step("admin user can navigate to ingest plans and verify draft plan for {cluster_name}")
def go_to_ingest_plan(context, cluster_name):
    admin_dashboard_page.goto_ingest_plans_list()
    admin_ingest_plans_list_page.verify_ingest_plan_list_page()
    admin_ingest_plans_list_page.search_and_land_to_change_ingest_plan(cluster_name)
    admin_ingest_plans_list_page.verify_ingest_plan_change_page()


@step("admin user can delete ingest draft plan created for cluster {cluster_name}")
def delete_ingest_plans(context, cluster_name):
    admin_dashboard_page.goto_ingest_plans_list()
    admin_ingest_plans_list_page.verify_ingest_plan_list_page()
    admin_ingest_plans_list_page.search_and_land_to_change_ingest_plan(cluster_name)
    admin_ingest_plans_list_page.verify_ingest_plan_change_page()
    admin_ingest_plans_list_page.delete_ingest_plan()
    admin_ingest_plans_list_page.verify_ingest_plan_list_page()


@step("admin user can navigate to ingest plans and get plan name for {cluster_name}")
def go_to_ingest_plan_to_get_plan_name(context, cluster_name):
    admin_dashboard_page.goto_ingest_plans_list()
    admin_ingest_plans_list_page.verify_ingest_plan_list_page()
    admin_ingest_plans_list_page.search_and_land_to_change_ingest_plan(cluster_name)
    admin_ingest_plans_list_page.verify_ingest_plan_change_page()
    admin_ingest_plans_list_page.go_to_dashboard_page()
    admin_dashboard_page.verify_login_pass()


@step('logged in user can rename cluster to {new_cluster_name}')
def create_cluster(context, new_cluster_name):
    blueprint_cluster_details_page.rename_cluster(new_cluster_name)
    blueprint_cluster_details_page.verify_cluster_details_page(new_cluster_name)


@step('user can verify status of the cluster as {cluster_status} from collection detail page')
def verify_cluster_status(context, cluster_status):
    blueprint_collection_details_page.verify_cluster_status("Cluster " + cluster_status)
