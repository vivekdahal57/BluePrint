Feature: User attempts to Login to Noble Application
  Scenario Outline: User fail to login in Blueprint
      Given user is in blueprint Login page
      When user use <username> and <password>
      Then user failed to login

   Examples: incorrect username and password
   | username | password |
   | test | test |
   | shailaza.dhakal@noble.ai | wrongpass |
   | @#$%##$% | #$%^$#@#%% |
   | wronguser | Winter20 |

  Scenario: User succeed to login in Blueprint
      Given user is in blueprint Login page
      When user use automation_user and Winter20
      Then user succeed to login
      Then user succeed to logout

  Scenario Outline: User fail to login in Django Admin
      Given user is in admin Login page
      When admin user use <username> and <password>
      Then admin user failed to login

   Examples: incorrect username and password
   | username | password |
   | test | test |
   | shailaza.dhakal@noble.ai | wrongpass |
   | @#$%##$% | #$%^$#@#%% |
   | wronguser | Winter20 |

  Scenario: User succeed to login in Django Admin
      Given user is in admin Login page
      When admin user use shailaza.dhakal@noble.ai and Winter20
      Then admin user succeed to login
      Then admin user succeed to logout