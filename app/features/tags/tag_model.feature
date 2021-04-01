Feature: Tag models tests
  Background:
    Given I have a user

  Scenario: Tag string representation should be it's name
    When I create a tag named "Vegan"
    Then My tags string representation is "Vegan"
