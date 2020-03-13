import time

from behave import step, runner
from page_object.global_objects import *


@step("admin user can delete {collection_name} collection")
def delete_collection(context, collection_name):
    admin_dashboard_page.goto_collection_list()
    admin_collection_list_page.search_and_land_to_change_collection(collection_name)
    admin_add_collection_page.verify_change_collection_page()
    admin_add_collection_page.delete_collection()
    admin_collection_list_page.verify_collections_list_page()


@step("admin user can delete {cluster_name} cluster")
def delete_cluster(context, cluster_name):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.delete_cluster()
    admin_cluster_list_page.verify_clusters_list_page()


@step(
    "admin user creates a cluster with name {cluster_name} cluster for {collection_name} collection and {status} status")
def create_cluster(context, cluster_name, collection_name, status):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.goto_add_cluster_page()
    admin_add_cluster_page.verify_add_cluster_page()
    admin_add_cluster_page.create_or_change_cluster(cluster_name, collection_name, status)
    admin_cluster_list_page.verify_cluster_list_page()


@step(
    "admin user can change a cluster with name {cluster_name} cluster for {collection_name} collection and {status} status")
def change_cluster(context, cluster_name, collection_name, status):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.create_or_change_cluster(cluster_name, collection_name, status)
    admin_cluster_list_page.verify_cluster_list_page()


@step("admin user can delete a cluster with name {cluster_name}")
def delete_cluster(context, cluster_name):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.delete_cluster()
    admin_cluster_list_page.verify_cluster_list_page()


@step("logged in user can search with filename {filename} and land on it")
def search_text(context, filename):
    blueprint_dashboard_page.search_and_land(filename)
    blueprint_ingested_document_page.verify_ingested_document_page()


@step("logged in user can search with collection name {collection_name} and lands on collection details page")
def search_collection(context, collection_name):
    blueprint_dashboard_page.verify_collection_and_land_on_detail(collection_name)
    blueprint_collection_details_page.verify_collection_details_page(collection_name)


@step("user lands on cluster detail page by searching {cluster_name} cluster name")
def search_cluster(context, cluster_name):
    blueprint_collection_details_page.click_element(blueprint_collection_details_page.dashboard_cluster_name_text)
    blueprint_cluster_details_page.verify_cluster_details_page(cluster_name)


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


@step("admin user can navigate to ingest result and verify completed ingest result")
def go_to_ingest_result(context):
    admin_dashboard_page.goto_ingest_results_list()
    admin_ingest_result_list_page.verify_ingest_result_list_page()
    admin_ingest_result_list_page.search_and_confirm_completed_ingest_result()


@step("user can download structured files from the collection details page")
def download_files(context):
    blueprint_collection_details_page.download_structured_file()
    time.sleep(5)
