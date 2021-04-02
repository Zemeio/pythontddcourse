Feature: Recipe models tests

  Background:
    Given I have a user

  Scenario: Recipe string representation should be it's name
    When I create recipes for my user with the following info:
      | title | time | price |
      | Pizza | 50   | 5.00  |
    Then The string representation of my recipe is "Pizza"
