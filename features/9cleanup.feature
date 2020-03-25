Feature: User attempts perform clean up for all created clusters and collections

  Scenario Outline: Admin user can delete draft ingest plan from admin panel
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can delete ingest draft plan created for cluster <cluster_name>
    Then admin user succeed to logout
    Examples: collection_names
      | cluster_name        |
      | automation_cluster1 |
      | automation_cluster2 |

  Scenario Outline: Created cluster can be deleted by admin user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can delete a cluster with name <cluster_name>
    Then admin user succeed to logout
    Examples: collection_names
      | cluster_name        |
      | automation_cluster1 |
      | automation_cluster2 |

  Scenario Outline: Created collection can be deleted by admin user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can delete <collection_name> collection
    Then admin user succeed to logout

    Examples: collection_names
      | collection_name                |
      | automation_collection1         |
      | automation_collection2         |
      | automation_collection3         |
      | automation_collection_docx     |
      | automation_collection_113pixel |
      | automation_collection_valid    |