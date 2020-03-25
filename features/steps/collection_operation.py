import os
import time

from behave import step
from page_object.global_objects import *


@step("admin user can delete {collection_name} collection")
def delete_collection(context, collection_name):
    admin_dashboard_page.goto_collection_list()
    admin_collection_list_page.search_and_land_to_change_collection(collection_name)
    admin_add_collection_page.verify_change_collection_page()
    admin_add_collection_page.delete_collection()
    admin_collection_list_page.verify_collections_list_page()


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


@step("logged in user can search with collection name {collection_name} and lands on collection details page")
def search_collection(context, collection_name):
    blueprint_dashboard_page.verify_collection_and_land_on_detail(collection_name)
    blueprint_collection_details_page.verify_collection_details_page(collection_name)


@step("user lands on cluster detail page by searching {cluster_name} cluster name")
def search_cluster(context, cluster_name):
    blueprint_collection_details_page.click_element(blueprint_collection_details_page.dashboard_cluster_name_text)
    blueprint_cluster_details_page.verify_cluster_details_page(cluster_name)


@step("user can download structured files from the collection details page")
def download_files(context):
    blueprint_collection_details_page.download_structured_file()
    time.sleep(5)


@step('logged in user can create collection with name {collection_name} and with file {file_name}')
def create_collection(context, collection_name, file_name):
    location = context.config.userdata.get('upload_file_location')
    if str(file_name.split("_")[0]).lower() == 'valid':
        location = os.path.join(context.config.userdata.get('upload_file_location'), 'validFiles')
    blueprint_dashboard_page.add_new_collection(os.path.join(location, file_name), collection_name)
    blueprint_collection_details_page.verify_collection_details_page(collection_name)
    blueprint_collection_details_page.verify_ingesting_bar(file_name)


@step('user cannot create collection with name {collection_name} with error generating file {file_name}')
def create_collection(context, collection_name, file_name):
    location = context.config.userdata.get('upload_file_location')
    if file_name.split("_")[0].lower() == "valid":
        location = os.path.join(context.config.userdata.get('upload_file_location'), 'validFiles')
    blueprint_dashboard_page.add_new_collection(os.path.join(location, file_name), collection_name)


@step('logged in user can rename collection to {new_collection_name}')
def create_collection(context, new_collection_name):
    blueprint_collection_details_page.rename_collection(new_collection_name)
    blueprint_collection_details_page.verify_collection_details_page(new_collection_name)


@step('user can sort collections in {sort_order} format')
def sorting(context, sort_order):
    blueprint_dashboard_page.sort_by_and_verify(sort_order)


@step("user can search collection with check {check_value} and valid filename {filename} and land on it")
def search_file_from_collection(context, filename, check_value):
    blueprint_collection_details_page.search_valid_file_and_land(filename, check_value)
    blueprint_ingested_document_page.verify_ingested_document_page()


@step("user can search collection with invalid filename {filename}")
def search_text(context, filename):
    blueprint_collection_details_page.search_invalid_file(filename)


@step('user can add file {file_name} in existing collection {collection_name}')
def create_collection(context, collection_name, file_name):
    location = context.config.userdata.get('upload_file_location')
    if file_name.split("_")[0].lower() == "valid":
        location = os.path.join(context.config.userdata.get('upload_file_location'), 'validFiles')
    blueprint_collection_details_page.add_file_to_existing_collection(os.path.join(location, file_name),
                                                                      collection_name)
    blueprint_collection_details_page.verify_collection_details_page(collection_name)


@step("user can navigate to Ingested documents and verify list of files {file_list} uploaded in {tab_name} tab")
def search_filename_from_dashboard(context, file_list, tab_name):
    blueprint_collection_details_page.goto_ingested_documents_page()
    blueprint_ingested_document_page.verify_ingested_document_page()
    blueprint_ingested_document_page.ingested_files_in_given_tab(tab_name, file_list.split(" "))


@step("user can navigate to Ingested documents and verify no files present in {tab_name} tab")
def search_filename_from_dashboard(context, tab_name):
    blueprint_collection_details_page.goto_ingested_documents_page()
    blueprint_ingested_document_page.verify_ingested_document_page()
    blueprint_ingested_document_page.ingested_files_in_given_tab(tab_name, [])
