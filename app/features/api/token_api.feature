@wip
Feature: Token test feature

  Background:
    Given I have a test client
    And I have the following users:
      | email          | username | password |
      | user@email.com | user     | password |

  Scenario: Token should be creatable for a user
    When I call the Create Token API for my user "user@email.com" with password "password"
    Then I get a 200 OK response
    And The response should contain the token keyword

  Scenario: Token should not be created if invalid credentials are given
    When I call the Create Token API for my user "user@email.com" with password "wrongpassword"
    Then I get a 400 BAD REQUEST response
    And The response should NOT contain the token keyword

  Scenario: Token should not be created if given user does not exist
    When I call the Create Token API for my user "wronguser@email.com" with password "password"
    Then I get a 400 BAD REQUEST response
    And The response should NOT contain the token keyword

  Scenario: Token should not be created if empty email is provided
    When I call the Create Token API without a user
    Then I get a 400 BAD REQUEST response
    And The response should NOT contain the token keyword

  Scenario: Token should not be created if empty password is provided
    When I call the Create Token API without a password
    Then I get a 400 BAD REQUEST response
    And The response should NOT contain the token keyword
