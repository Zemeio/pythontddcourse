Feature: Test recipe API

  Background:
    Given I have an API test client
    And I have a user
    And My test client is authenticated for my user

  Scenario: Calling the API with a get should return a list of recipes
    Given I have recipes for my user with the following info:
      | title  | time | price |
      | Pizza  | 50   | 5.00  |
      | Pizza2 | 50   | 5.00  |
    When I call the recipe list API
    Then I get a 200 OK response
    And All of the recipes are returned sorted by id

  Scenario: Calling the API with a get should return only the recipes of the authenticated user
    Given I have the following users:
      | email               | username  | password |
      | otheruser@email.com | otheruser | password |
    And I have recipes for my user with the following info:
      | title | time | price |
      | Pizza | 50   | 5.00  |
    And I have recipes for the user "otheruser@email.com" with the following info:
      | title  | time | price |
      | Esfiha | 50   | 5.00  |
    When I call the recipe list API
    Then I get a 200 OK response
    And The response contains "1" key
    And The recipe for "Pizza" should appear in the result
