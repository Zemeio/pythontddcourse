Feature: User api tests that require authentication

  Background:
    Given I have an API test client
    And I have the following users:
      | email          | username | password |
      | user@email.com | user     | password |
    And My test client is authenticated for user "user@email.com"


  Scenario: User should be able to retrieve his profile after logging in
    When I call the ME API
    Then I get a 200 OK response
    And The response contains the email "user@email.com"
    And The response contains the name "user"

  Scenario: Post method should not be allowed for the ME endpoint
    When I call the ME API with the post method
    Then I get a 405 METHOD NOT ALLOWED response

  Scenario: Authenticated user should be able to update their profile
    When I call the ME API with the following payload:
      | username | password    |
      | newuser  | newpassword |
    And The DB is refreshed for the user "user@email.com"
    Then I get a 200 OK response
    And User "user@email.com" has name "newuser"
    And User "user@email.com" has password "newpassword"
