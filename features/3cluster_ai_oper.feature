Feature: User attempts perform cluster and collection operation

  Scenario: User creates a collection
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can create collection with name automation_collection1 and with file img.PNG
    Then user succeed to logout

  Scenario: Admin User able to create cluster
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user creates a cluster with name automation_cluster1 cluster for automation_collection1 collection and Pending status
    Then admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Active status
    Then admin user can delete a cluster with name automation_cluster1

  Scenario: Created collection can be deleted by admin user
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user can delete automation_collection1 collection
