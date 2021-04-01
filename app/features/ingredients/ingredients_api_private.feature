Feature: Test ingredient API that require authorization

  Background:
    Given I have an API test client
    And I have a user
    And My test client is authenticated for my user

  Scenario: Ingredient API should return a list of ingredients
    Given I have an ingredient associated with my user named "Salt"
    And I have an ingredient associated with my user named "Kale"
    When I call the ingredient list API
    Then I get a 200 OK response
    And All of my ingredients are in the response ordered by name

  Scenario: Retrieve ingredients should return only the ingredients of the user authenticated
    Given I have an ingredient associated with my user named "Salt"
    And I have the following users:
      | email          | username | password |
      | user@email.com | user     | password |
    And I have an ingredient "Pepper" for the user "user@email.com"
    When I call the ingredient list API
    Then I get a 200 OK response
    And The response contains "1" key
    And the ingredient "Salt" is returned in the response

  Scenario: Create Ingredient should create ingredients for the authenticated user
    When I call the Ingredient API with the following payload:
      | name |
      | Salt |
    Then Ingredient with name "Salt" exists in the database for my user

  Scenario: Create Ingredient should fail for empty ingredient name
    When I call the Ingredient API with an empty name
    Then I get a 400 BAD REQUEST response
