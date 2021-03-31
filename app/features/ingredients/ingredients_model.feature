Feature: Test ingredients endpoint models

  Scenario: Ingredients string representation should be it's name
    Given I have a user
    And I have an ingredient associated with my user named "Cucumber"
    When I take the string representation of my ingredient
    Then The string representation is "Cucumber"
