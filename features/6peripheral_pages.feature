Feature: User attempts to browser and verify all blueprint peripheral pages

  Scenario: Normal user can navigate to User Manual page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user navigate to User Manual page
    Then user succeed to logout

  Scenario: Normal user can navigate to FAQ page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user navigate to FAQ page
    Then user succeed to logout

  Scenario: Normal user can navigate to Terms of Service page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user navigate to Terms of Service page
    Then user succeed to logout

  Scenario: Normal user can navigate to Privacy and Terms page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user navigate to Google Analytics page
    Then user succeed to logout