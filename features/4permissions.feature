Feature: User Permission tests

  Scenario: User creates a collection with suffix no_per
    Given user is in blueprint Login page
    When user use created_username and created_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection_no_per and with file goodtxt.txt
    Then user succeed to logout

  Scenario: Admin User is able to create cluster with suffix no_per
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a cluster with name automation_cluster_no_per cluster for automation_collection_no_per collection and Pending status
    Then admin user can change a cluster with name automation_cluster_no_per cluster for automation_collection_no_per collection and Proposed status
    Then admin user succeed to logout

  Scenario: User search for automation_collection_no_per in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use created_username and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then user succeed to logout

  Scenario: Staff User can assign batch to the cluster_no_per
    Given user is in blueprint Login page
    When user use admin_username and admin_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user can drag transfer-batch to automation_cluster_no_per after selecting automation_collection_no_per
    Then user can create a draft plan for collection automation_collection_no_per and for cluster automation_cluster_no_per
    Then user can create a new step with Bounding Box for goodtxt.txt file for collection automation_collection_no_per and cluster automation_cluster_no_per
    Then user succeed to logout from architect application

  Scenario: Admin user can verify draft ingest plan from admin panel for cluster_no_per
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can navigate to ingest plans and verify draft plan for automation_cluster_no_per
    Then admin user succeed to logout

  Scenario: Admin User is able to update cluster_no_per
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can change a cluster with name automation_cluster_no_per cluster for automation_collection_no_per collection and Active status
    Then admin user succeed to logout

  Scenario: User search for collection_no_per in dashboard and download file
    Given user is in blueprint Login page
    When user use created_username and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then user can download structured files from the collection details page using created_password
    Then user succeed to logout

  Scenario: User search for automation_collection_no_per in dashboard but do not lands on details page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and verify not present
    Then user succeed to logout

  Scenario: Admin User able to create a new group with name Automation_Group
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can create a group with name Automation_Group
    Then admin user succeed to logout

  Scenario: Admin User able to assign group to users
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can assign group Automation_Group to username correct_username
    Then admin user can assign group Automation_Group to username created_username
    Then admin user succeed to logout

  Scenario: Admin User able to assign group to collection
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can assign a group with name Automation_Group to the collection automation_collection_no_per
    Then admin user succeed to logout

  Scenario: User search for automation_collection_no_per in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then user succeed to logout

  Scenario: Admin User able to unselect assigned group from user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user unselect group Automation_Group for username correct_username
    Then admin user succeed to logout
    Then user with username correct_username and password correct_password is able to login
    Then user succeed to logout

  Scenario: Created group can be deleted by admin user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can delete Automation_Group group
    Then admin user succeed to logout

  Scenario: Admin User able to assign group to collection
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can assign a group with name Everyone to the collection automation_collection_no_per
    Then admin user succeed to logout

  Scenario: Admin User able to create Active user with suffix 2
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a inactive user with username automation_user2 and password created_password
    And admin user changes a inactive user to active with username automation_user2
    Then admin user succeed to logout

  Scenario: User 2 search for automation_collection_no_per in dashboard and lands on details page
    Given user is in blueprint Login page
    When user use automation_user2 and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then user succeed to logout

  Scenario: User2 search for collection_no_per in dashboard and download file
    Given user is in blueprint Login page
    When user use automation_user2 and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then user can download structured files from the collection details page using created_password
    Then user succeed to logout

  Scenario: User2 renames a collection with suffix no_per to everyone
    Given user is in blueprint Login page
    When user use automation_user2 and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_no_per and lands on collection details page
    Then logged in user can rename collection to automation_collection_everyone
    Then user succeed to logout

  Scenario: User2 add new file in existing collection
    Given user is in blueprint Login page
    When user use automation_user2 and created_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_everyone and lands on collection details page
    Then user can add file img.PNG in existing collection automation_collection_everyone
    Then user succeed to logout