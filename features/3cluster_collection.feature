Feature: User attempts perform cluster and collection operation

  Scenario: User creates a collection with suffix old
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection_old and with file pdffile.pdf
    Then user succeed to logout

  Scenario: User renames a collection with suffix old to 1
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_old and lands on collection details page
    Then logged in user can rename collection to automation_collection1
    Then user succeed to logout

  Scenario: Admin User is able to create cluster with suffix old
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a cluster with name automation_cluster_old cluster for automation_collection1 collection and Pending status
    Then admin user can change a cluster with name automation_cluster_old cluster for automation_collection1 collection and Proposed status
    Then admin user succeed to logout

  Scenario: User search for automation_collection1 in dashboard and rename cluster with suffix old to suffix 1
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user lands on cluster detail page by searching automation_cluster_old cluster name
    Then logged in user can rename cluster to automation_cluster1
    Then user succeed to logout

  Scenario: User find automation_collection1 in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection1 and lands on collection details page
    Then user succeed to logout

  Scenario: User search for file from blueprint dashboard page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with filename pdffile.pdf and land on it
    Then user succeed to logout

  Scenario: User creates a collection with suffix 2
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection2 and with file zipfile.zip
    Then user succeed to logout

  Scenario: Admin User is able to create cluster with suffix 2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a cluster with name automation_cluster2 cluster for automation_collection2 collection and Pending status
    Then admin user succeed to logout

  Scenario: User find automation_collection2 in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user succeed to logout

  Scenario: User search for existing file from automation_collection2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can search collection with check True and valid filename img.PNG and land on it
    Then user succeed to logout

  Scenario: User search for non existing file from automation_collection2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can search collection with invalid filename pdffile.pdf
    Then user succeed to logout

  Scenario: User search for file present in different automation_collection1 from automation_collection2 detail page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can search collection with check False and valid filename pdffile.pdf and land on it
    Then user succeed to logout

  Scenario Outline: User can view files in routing tab for existing collection with suffix 2
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can navigate to Ingested documents and verify list of files <file_list> uploaded in Routing tab
    Then user succeed to logout
    Examples: Some example
      | file_list                       |
      | img.PNG goodpdf.pdf XlsTest.xls |
