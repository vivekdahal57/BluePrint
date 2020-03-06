Feature: User attempts to perform ingest and organize operation in ai tool

  Scenario: Staff User can assign batch to the cluster
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster1 after selecting automation_collection1
    Then user succeed to logout from architect application

  Scenario: Staff User can create draft ingest plan
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a draft plan for collection automation_collection1 and for cluster automation_cluster1
    Then user succeed to logout from architect application

  Scenario: Admin user can verify draft ingest plan from admin panel
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster1
    Then admin user succeed to logout

  Scenario: Staff User can ingest and activate ingest plan
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can create a new step with Bounding Box for img.PNG file for collection automation_collection1 and cluster automation_cluster1
    Then user succeed to logout from architect application
