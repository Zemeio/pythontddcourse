Feature: Test recipe API
  Background:
    Given I have an API test client

  Scenario: Calling the API without logging in should give an error
    When I call the recipe list API
    Then I get a 401 UNAUTHORIZED response
