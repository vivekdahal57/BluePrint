 Feature: User attempts perform clean up for all created clusters and collections

  Scenario: Created cluster can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete a cluster with name automation_cluster1

  Scenario: Created collection can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete automation_collection1 collection