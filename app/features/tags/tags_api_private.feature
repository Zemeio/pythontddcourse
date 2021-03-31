Feature: Tests from tags that require authentication

  Background:

    Given I have a user
    And I have an API test client
    And My test client is authenticated for my user

  Scenario: Retrieve tags should return a list of tags for the current user
    Given I have a tag named "Vegan"
    And I have a tag named "Desert"
    When I call the tag list API
    Then I get a 200 OK response
    And All of my tags are in the response ordered by name

  Scenario: Retrieve tags should return only the tags of the user authenticated
    Given I have a tag named "Vegan"
    And I have the following users:
      | email          | username | password |
      | user@email.com | user     | password |
    And I have a tag "Fruity" for the user "user@email.com"
    When I call the tag list API
    Then I get a 200 OK response
    And The response contains "1" key
    And the tag "Vegan" is returned in the response

  Scenario: Create tag should return success
    When I call the tag API with the following payload:
      | name     |
      | Test Tag |
    Then I get a 201 CREATED response
    And Tag with name "Test Tag" exists in the database for my user

  Scenario: Create tag should fail for empty name
    When I call the tag API with an empty name
    Then I get a 400 BAD REQUEST response

