 Feature: User attempts perform clean up for all created clusters and collections

  Scenario: Created cluster can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete a cluster with name automation_cluster1

  Scenario Outline: Created collection can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete <collection_name> collection

    Examples: collection_names
      | collection_name|
      | automation_collection1|
      | automation_collection2|
