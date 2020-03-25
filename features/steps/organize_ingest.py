from behave import step

from page_object.global_objects import *


@step('user can drag transfer-batch to {cluster_name} after selecting {collection_name}')
def drag_n_drop_to_cluster(context, collection_name, cluster_name):
    architect_dashboard_page.select_collection(collection_name)
    architect_dashboard_page.drag_transfer_batch_to_cluster(cluster_name)


@step('user succeed to logout from architect application')
def pass_login(context):
    architect_dashboard_page.logout()


@step('user can create a draft plan for collection {collection_name} and for cluster {cluster_name}')
def create_draft_ingest_plan(context, collection_name, cluster_name):
    architect_dashboard_page.go_to_ingest_page()
    architect_ingest_page.verify_ingest_dashboard()
    architect_ingest_page.expand_collection(collection_name)
    architect_ingest_page.select_cluster_and_create_draft(cluster_name)
    architect_ingest_page.verify_ingest_draft_plan()


@step(
    'user can create a new step with {step_type} for {file_name} file for collection {collection_name} and cluster {cluster_name}')
def create_draft_ingest_plan(context, step_type, file_name, collection_name, cluster_name):
    url = context.web.get_current_url()
    if "ingest" not in url.split("/"):
        architect_dashboard_page.go_to_ingest_page()
        architect_ingest_page.verify_ingest_dashboard()
        architect_ingest_page.expand_collection(collection_name)
        architect_ingest_page.select_cluster(cluster_name)
    architect_ingest_page.make_file_staged(file_name)
    architect_ingest_page.create_new_step(step_type, "Auto_step")
    architect_ingest_page.verify_ingested_file(file_name)


@step("admin user can navigate to ingest result and verify completed ingest result")
def go_to_ingest_result(context):
    admin_dashboard_page.goto_ingest_results_list()
    admin_ingest_result_list_page.verify_ingest_result_list_page()
    admin_ingest_result_list_page.search_and_confirm_completed_ingest_result()
