from behave import step, runner

from page_object.global_objects import architect_dashboard_page, architect_ingest_page


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


@step('user can create a new step with {step_type} for {file_name} file for collection {collection_name} and cluster {cluster_name}')
def create_draft_ingest_plan(context, step_type, file_name,collection_name, cluster_name):
    architect_dashboard_page.go_to_ingest_page()
    architect_ingest_page.verify_ingest_dashboard()
    architect_ingest_page.expand_collection(collection_name)
    architect_ingest_page.select_cluster(cluster_name)
    architect_ingest_page.make_file_staged(file_name)
    architect_ingest_page.create_new_step(step_type, "Auto_step")
    architect_ingest_page.verify_ingested_file(file_name)
