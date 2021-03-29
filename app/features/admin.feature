Feature: Admin feature tests

  Background:
    Given I have a test client
    And I have a user logged in
    And I have a regular user unauthenticated

  Scenario: Users should be listed in django-admin
    When I access the "admin core user changelist" page
    Then My regular user appears in the response

  Scenario: User edit page should be accessible for our regular user
    When I access the edit user page for my regular user
    Then I get a 200 OK response

  Scenario: User create page should be accessible
    When I access the create user page
    Then I get a 200 OK response
