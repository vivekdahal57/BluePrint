Feature: Admin User attempts perform users crud operation

  Scenario: Admin User able to create inactive staff user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a inactive user with username staff_username and password staff_password
    Then admin user succeed to logout
    Then inactive user with username staff_username and password staff_password is not able to login

  Scenario: Admin User able to edit inactive staff user to active
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user changes a inactive user to active with username staff_username
    Then admin user succeed to logout
    Then user with username staff_username and password staff_password is able to login
    Then user succeed to logout

  Scenario: Staff User can navigate to architect application
    Given user is in blueprint Login page
    When user use staff_username and staff_password
    Then user succeed to login
    Then user navigate to Architect application
    Then user succeed to logout from architect application

  Scenario: Admin User able to create inactive user
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a inactive user with username created_username and password created_password
    Then admin user succeed to logout
    Then inactive user with username created_username and password created_password is not able to login

  Scenario: Admin User able to edit inactive user to active
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user changes a inactive user to active with username created_username
    Then admin user succeed to logout
    Then user with username created_username and password created_password is able to login
    Then user succeed to logout

  Scenario: Created user land on dashboard by clicking I accept
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a user profile with username created_username
    Then admin user succeed to logout
    Then user with username created_username and password created_password is able to login
    Then user succeed to logout