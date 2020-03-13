Feature: User attempts to perform ingest and organize operation in ai tool

  Scenario: Staff User can assign batch to the cluster1
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster1 after selecting automation_collection1
    Then user succeed to logout from architect application

  Scenario: Staff User can assign batch to the cluster2
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster2 after selecting automation_collection2
    Then user succeed to logout from architect application

  Scenario: Staff User can create draft ingest plan for cluster1
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a draft plan for collection automation_collection1 and for cluster automation_cluster1
    Then user succeed to logout from architect application

  Scenario: Staff User can create draft ingest plan for cluster2
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a draft plan for collection automation_collection2 and for cluster automation_cluster2
    Then user succeed to logout from architect application

  Scenario: Admin user can verify draft ingest plan from admin panel for cluster1
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster1
    Then admin user succeed to logout

  Scenario: Admin user can verify draft ingest plan from admin panel for cluster2
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster2
    Then admin user succeed to logout

  Scenario: Staff User can ingest and activate ingest plan for cluster1
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a new step with Bounding Box for pdffile.pdf file for collection automation_collection1 and cluster automation_cluster1
    Then user succeed to logout from architect application

  Scenario: Staff User can ingest and activate ingest plan for cluster2
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a new step with Bounding Box for img.PNG file for collection automation_collection2 and cluster automation_cluster2
    Then user succeed to logout from architect application

  Scenario: Admin user can verify completed ingested result from admin panel for cluster1
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can navigate to ingest plans and get plan name for automation_cluster1
    Then admin user can navigate to ingest result and verify completed ingest result
    Then admin user succeed to logout

  Scenario: Admin user can verify completed ingested result from admin panel for cluster2
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can navigate to ingest plans and get plan name for automation_cluster2
    Then admin user can navigate to ingest result and verify completed ingest result
    Then admin user succeed to logout

  Scenario: Admin User is able to update cluster1
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Active status
    Then admin user succeed to logout

  Scenario: Admin User is able to update cluster2
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can change a cluster with name automation_cluster2 cluster for automation_collection2 collection and Active status
    Then admin user succeed to logout

  Scenario: User search for collection1 in dashboard and download file
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user can download structured files from the collection details page
    Then user succeed to logout

  Scenario: User search for collection2 in dashboard and download file
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can download structured files from the collection details page
    Then user succeed to logout
