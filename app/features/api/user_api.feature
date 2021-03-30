Feature: Test user API

  Background:
    Given I have a test client

  Scenario: User is created successfully
    When I call the Create User API with the following payload:
      | email          | username | password |
      | user@email.com | user     | password |
    Then I get a 201 CREATED response
    And The user exists in my model
    And User password is "password"
    And Password is not returned in the API response

  Scenario Outline: Adding existing email should return an error
    Given I have the following users:
      | email          | username | password |
      | user@email.com | user     | password |
    When I call the Create User API with the following payload:
      | email          | username   | password   |
      | user@email.com | <username> | <password> |
    Then I get a 400 BAD REQUEST response
    Examples:
      | username      | password          |
      | user          | password          |
      | differentuser | password          |
      | user          | differentpassword |
      | differentuser | differentpassword |

  Scenario: Should fail if password has fewer than 5 characters
    When I call the Create User API with the following payload:
      | email          | username | password |
      | user@email.com | user     | pw       |
    Then I get a 400 BAD REQUEST response
    And The user "user@email.com" does not exist in my model
