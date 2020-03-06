Feature: User attempts perform clean up for all created clusters and collections

  Scenario: Admin user can delete draft ingest plan from admin panel
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete ingest draft plan created for cluster automation_cluster1
    Then admin user succeed to logout

  Scenario: Created cluster can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete a cluster with name automation_cluster1
    Then admin user succeed to logout

  Scenario Outline: Created collection can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete <collection_name> collection
    Then admin user succeed to logout

    Examples: collection_names
      | collection_name        |
      | automation_collection1 |
      | automation_collection2 |