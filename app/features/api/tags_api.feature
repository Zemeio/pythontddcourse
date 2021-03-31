Feature: Test recipe API
  Background:
    Given I have an API test client

  Scenario: Login should be required to retrieve tags
    When I call the tag list API
    Then I get a 401 UNAUTHORIZED response
