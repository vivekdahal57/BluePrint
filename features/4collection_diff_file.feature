Feature: User attempts perform collection operation with different files

  Scenario: User creates a collection with file size above 500mb
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection3 and with file too_large.zip
    Then user succeed to logout

  Scenario: User add new file in existing collection with suffix 3
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection3 and lands on collection details page
    Then user can add file zipfile.zip in existing collection automation_collection3
    Then user succeed to logout

  Scenario: User creates a collection with file size above 2gb
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user cannot create collection with name automation_collection4 with error generating file 2GB_large.zip
    Then user succeed to logout

  Scenario: User creates a collection with empty file
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user cannot create collection with name automation_collection4 with error generating file Hello.mfg
    Then user succeed to logout

  Scenario: User creates a collection with unknown extension
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user cannot create collection with name automation_collection4 with error generating file test.rug
    Then user succeed to logout

  Scenario: User creates a collection with docx
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection_docx and with file docx.docx
    Then user succeed to logout

  Scenario: Admin User is able to create cluster for docx collection
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user creates a cluster with name automation_cluster_docx cluster for automation_collection_docx collection and Pending status
    Then admin user can change a cluster with name automation_cluster_docx cluster for automation_collection_docx collection and Proposed status
    Then admin user succeed to logout

  Scenario: User can verify Proposed Status of cluster for docx collection
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_docx and lands on collection details page
    Then user can verify status of the cluster as Proposed from collection detail page
    Then user succeed to logout

  Scenario: Admin User is able to update cluster for docx collection
    Given admin user is in dashboard page after login with admin_username and admin_password
    When admin user can change a cluster with name automation_cluster_docx cluster for automation_collection_docx collection and Queued status
    Then admin user succeed to logout

  Scenario: User can verify Queued Status of cluster for docx collection
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_docx and lands on collection details page
    Then user can verify status of the cluster as Queued from collection detail page
    Then user succeed to logout

  Scenario: User creates a collection with valid files
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection_valid and with file valid_small.tar
    Then user succeed to logout

  Scenario Outline: User add new valid files in existing collection
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_valid and lands on collection details page
    Then user can add file <valid_file> in existing collection automation_collection_valid
    Then user succeed to logout
    Examples:
      | valid_file          |
      | valid_too_large.zip |
      | valid_8mb.zip       |
      | valid_93pixels.png  |
      | valid_medium.zip    |
      | valid_small.zip     |

  Scenario: User creates a collection with 113pixels img file
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can create collection with name automation_collection_113pixel and with file 113pixels.png
    Then user succeed to logout

  Scenario: User can verify no files in Routing tab for existing collection for 112m pixel file is uploaded
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then logged in user can search with collection name automation_collection_113pixel and lands on collection details page
    Then user can navigate to Ingested documents and verify no files present in Routing tab
    Then user succeed to logout

  Scenario: User can sort collections in new to old format
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user can sort collections in new to old format
    Then user succeed to logout

  Scenario: User can sort collections in old to new format
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user can sort collections in old to new format
    Then user succeed to logout

  Scenario: User can sort collections in high to low format
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user can sort collections in high to low format
    Then user succeed to logout

  Scenario: User can sort collections in low to high format
    Given user is in blueprint Login page
    When user use correct_username and correct_password
    Then user succeed to login
    Then user can sort collections in low to high format
    Then user succeed to logout

