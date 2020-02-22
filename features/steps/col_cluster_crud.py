from behave import step
from page_object.global_objects import *


@step("admin user can delete {collection_name} collection")
def delete_collection(context, collection_name):
    admin_dashboard_page.goto_collection_list()
    admin_collection_list_page.search_and_land_to_change_collection(collection_name)
    admin_add_collection_page.verify_change_collection_page()
    admin_add_collection_page.delete_collection()
    admin_collection_list_page.verify_collections_list_page()
    admin_dashboard_page.logout()


@step("admin user can delete {cluster_name} cluster")
def delete_cluster(context, cluster_name):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.delete_cluster()
    admin_cluster_list_page.verify_clusters_list_page()
    admin_dashboard_page.logout()


@step(
    "admin user creates a cluster with name {cluster_name} cluster for {collection_name} collection and {status} status")
def create_cluster(context, cluster_name, collection_name, status):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.goto_add_cluster_page()
    admin_add_cluster_page.verify_add_cluster_page()
    admin_add_cluster_page.create_or_change_cluster(cluster_name, collection_name, status)
    admin_cluster_list_page.verify_cluster_list_page()
    # admin_dashboard_page.logout()


@step(
    "admin user can change a cluster with name {cluster_name} cluster for {collection_name} collection and {status} status")
def change_cluster(context, cluster_name, collection_name, status):
    # admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.create_or_change_cluster(cluster_name, collection_name, status)
    admin_cluster_list_page.verify_cluster_list_page()
    # admin_dashboard_page.logout()


@step("admin user can delete a cluster with name {cluster_name}")
def delete_cluster(context, cluster_name):
    admin_dashboard_page.goto_cluster_list()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_cluster_list_page.search_and_land_to_change_cluster(cluster_name)
    admin_add_cluster_page.verify_change_cluster_page()
    admin_add_cluster_page.delete_cluster()
    admin_cluster_list_page.verify_cluster_list_page()
    admin_dashboard_page.logout()


@step("logged in user can search with filename {filename} and land on it")
def search_text(context, filename):
    blueprint_dashboard_page.search_and_land(filename)
    blueprint_ingested_document_page.verify_ingested_document_page()
