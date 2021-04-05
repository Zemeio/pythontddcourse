@wip
Feature: Recipe Detail View Tests

  Background:
    Given I have an API test client
    And I have a user
    And My test client is authenticated for my user

  Scenario: Recipe detail should return information of the recipe with expanded fields instead of only IDs
    Given I have recipes for my user with the following info:
      | title | time | price |
      | Pizza | 50   | 5.00  |
    And Recipe "Pizza" has a tag named "Food"
    And I have an ingredient associated with my user named "\{ingredient_name\}"
    When I call the recipe detail API for recipe "Pizza"
    Then The response should contain be equal to the "Pizza" recipe in the database
