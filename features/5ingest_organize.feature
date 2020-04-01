Feature: User attempts to perform ingest and organize operation in ai tool

  Scenario: Staff User can assign batch to the cluster1
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster1 after selecting automation_collection1
    Then user succeed to logout from architect application

  Scenario: Staff User can create draft ingest plan for cluster1
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a draft plan for collection automation_collection1 and for cluster automation_cluster1
    Then user succeed to logout from architect application

  Scenario: Admin user can verify draft ingest plan from admin panel for cluster1
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster1
    Then admin user succeed to logout

  Scenario: Staff User can ingest and activate ingest plan for cluster1
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a new step with Bounding Box for pdffile.pdf file for collection automation_collection1 and cluster automation_cluster1
    Then user succeed to logout from architect application

  Scenario: Admin user can verify completed ingested result from admin panel for cluster1
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can navigate to ingest plans and get plan name for automation_cluster1
    Then admin user can navigate to ingest result and verify completed ingest result
    Then admin user succeed to logout

  Scenario: Admin User is able to update cluster1
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Active status
    Then admin user succeed to logout

  Scenario: User search for collection1 in dashboard and download file
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user can download structured files from the collection details page using correct_password
    Then user succeed to logout

  Scenario: Staff User can assign batch to the cluster2
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster2 after selecting automation_collection2
    Then user succeed to logout from architect application

  Scenario: User can verify no files in Routing tab for existing collection with suffix 2 after transfer batch is assigned to cluster
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can navigate to Ingested documents and verify no files present in Routing tab
    Then user succeed to logout

  Scenario Outline: User can view files in New Doc Type tab for existing collection with suffix 2 after transfer batch is assigned to cluster
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can navigate to Ingested documents and verify list of files <file_list> uploaded in New Doc Type tab
    Then user succeed to logout
    Examples: Some example
      | file_list                       |
      | img.PNG goodpdf.pdf XlsTest.xls |

  Scenario: Admin User is able to update cluster with Proposed status for suffix 2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can change a cluster with name automation_cluster2 cluster for automation_collection2 collection and Proposed status
    Then admin user succeed to logout

  Scenario: User finds automation_collection2 in dashboard and lands on cluster detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster2 cluster name
    Then user succeed to logout

  Scenario: User can verify no files in Routing tab for existing collection with suffix 2 after cluster is updated to Proposed
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can navigate to Ingested documents and verify no files present in Routing tab
    Then user succeed to logout

  Scenario: User can verify no files in Routing tab for existing collection with suffix 2 after cluster is updated to Proposed
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can navigate to Ingested documents and verify no files present in New Doc Type tab
    Then user succeed to logout

  Scenario: Staff User can create draft ingest plan for cluster2
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a draft plan for collection automation_collection2 and for cluster automation_cluster2
    Then user succeed to logout from architect application

  Scenario: Admin user can verify draft ingest plan from admin panel for cluster2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster2
    Then admin user succeed to logout

  Scenario: Staff User can ingest and activate ingest plan for cluster2
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a new step with Bounding Box for img.PNG file for collection automation_collection2 and cluster automation_cluster2
    Then user succeed to logout from architect application

  Scenario: Admin user can verify completed ingested result from admin panel for cluster2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can navigate to ingest plans and get plan name for automation_cluster2
    Then admin user can navigate to ingest result and verify completed ingest result
    Then admin user succeed to logout

  Scenario: Admin User is able to update cluster2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can change a cluster with name automation_cluster2 cluster for automation_collection2 collection and Active status
    Then admin user succeed to logout

  Scenario: User search for collection2 in dashboard and download file
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can download structured files from the collection details page using correct_password
    Then user succeed to logout

# Searching in cluster is possible only after transfer batch is moved to the cluster
  Scenario: User search for existing file from automation_cluster2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster2 cluster name
    Then user can search cluster with collection check True, cluster check True and valid filename img.PNG and land on automation_cluster2 page
    Then user succeed to logout

  Scenario: User search for non existing file from automation_cluster2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster2 cluster name
    Then user can search cluster with invalid filename pdffile.pdf
    Then user succeed to logout

  Scenario: User search for existing file in different collection automation_cluster2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster2 cluster name
    Then user can search cluster with collection check False, cluster check False and valid filename pdffile.pdf and land on automation_cluster1 page
    Then user succeed to logout
