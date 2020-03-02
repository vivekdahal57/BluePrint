Feature: User attempts perform cluster and collection operation

  Scenario: User creates a collection with suffix 1
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can create collection with name automation_collection1 and with file img.PNG
    Then user succeed to logout

  Scenario: User creates a collection with suffix 2
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can create collection with name automation_collection2 and with file XlsTest.xls
    Then user succeed to logout

  Scenario: Admin User is able to create cluster
    Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
    When admin user creates a cluster with name automation_cluster1 cluster for automation_collection1 collection and Pending status
    Then admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Active status
    Then admin user succeed to logout

  Scenario: User search for files in the collection
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can search with filename img.PNG and land on it
    Then user succeed to logout

  Scenario: User search for collection in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user succeed to logout

  Scenario: User search for collection in dashboard and lands on cluster detail page
    Given user is in blueprint Login page
    When user use automation_user and Winter20
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster1 cluster name
    Then user succeed to logout

  Scenario: Staff User can assign batch to the cluster
    Given user is in blueprint Login page
    When user use shailaza.dhakal@noble.ai and Winter20
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster1 after selecting automation_collection1
    Then user succeed to logout from architect application
