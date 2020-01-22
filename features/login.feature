Feature: User attempts to Login to Noble Application
  Scenario Outline: User fail to login in Blueprint
      Given user is in Login page
      When user use <username> and <password>
      Then user failed to login

   Examples: incorrect username and password
   | username | password |
   | test | test |
   | shailaza.dhakal@noble.ai | wrongpass |
   | @#$%##$% | #$%^$#@#%% |
   | wronguser | Winter20 |

  Scenario: User succeed to login in Blueprint
      Given user is in Login page
      When user use shailaza.dhakal@noble.ai and Winter20
      Then user succeed to login