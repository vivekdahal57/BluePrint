Feature: Admin User attempts perform users crud operation
  Scenario: Admin User able to create user
      Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
      When admin user creates a user with username automation_user1 and password Password#1
      Then user with username automation_user1 and password Password#1 is able to login and logout

  Scenario: Created user land on dashboard by clicking I accept
      Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
      When admin user creates a user profile with username automation_user1
      Then user with username automation_user1 and password Password#1 is able to login and logout

  Scenario: Created user can be deleted by admin user
      Given admin user is in dashboard page after login with shailaza.dhakal@noble.ai and Winter20
      When admin user can delete automation_user1 user
      Then deleted user with username automation_user1 and password Password#1 cannot login