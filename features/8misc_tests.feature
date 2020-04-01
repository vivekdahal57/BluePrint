Feature: User attempts perform collection operation with different files

  Scenario: User search for Untitled Collection in dashboard but do not lands on details page
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name Untitled Collection and lands on collection details page
    Then user succeed to logout

  Scenario: User input URL with http changes to https automatically
    Given user is in blueprint Login page
    When user reapply blueprint url with http
    Then url changes to https automatically

  Scenario: User click back button on the browser during file upload
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user click back button in a browser during file upload of valid_too_large.zip

  Scenario: User2 search for automation_collection2 in dashboard and download file
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection2 and lands on collection details page
    Then user can click back button during download structured files from the collection details page using correct_password
    Then user succeed to logout