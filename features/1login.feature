Feature: User attempts to Login to Noble Application. Also creates Periodic tasks and let it execute.

  Scenario: Admin User able to create and run a new periodic task with name Automation_Task0
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can create a periodic task with name Automation_Task0 and enable False status
    Then admin user succeed to logout

  Scenario: Admin User able to update the periodic task with start and expiry time
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can enable True to Automation_Task0 periodic task with start end datetime
    Then admin user succeed to logout

  Scenario: Admin User able to create and run a new periodic task with name Automation_Task1
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can create a periodic task with name Automation_Task1 and enable False status
    Then admin user can run the periodic task Automation_Task1 from list page
    Then admin user succeed to logout

  Scenario Outline: User fail to login in Blueprint
    Given user is in blueprint Login page
    When user use <username> and <password>
    Then user failed to login

    Examples: incorrect username and password
      | username                 | password   |
      | test                     | test       |
      | shailaza.dhakal@noble.ai | wrongpass  |
      | @#$%##$%                 | #$%^$#@#%% |
      | wronguser                | Winter20   |
      | Blank                    | Blank      |

  Scenario: User succeed to login in Blueprint
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user succeed to logout

  Scenario Outline: User fail to login in Django Admin
    Given user is in admin Login page
    When admin user use <username> and <password>
    Then admin user failed to login

    Examples: incorrect username and password
      | username                 | password   |
      | test                     | test       |
      | shailaza.dhakal@noble.ai | wrongpass  |
      | @#$%##$%                 | #$%^$#@#%% |
      | wronguser                | Winter20   |
      | Blank                    | Blank      |

  Scenario: User succeed to login in Django Admin
    Given user is in admin Login page
    When admin user use admin_username and admin_password
    Then admin user succeed to login
    Then admin user succeed to logout

  Scenario: Normal User cannot access admin panel
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user is in admin Login page
    Then normal user correct_username failed to authorized