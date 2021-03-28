Feature: User Feature

  Scenario: User can be created
    When a user has been created with the following details:
       | email          | username  | password |
       | user@email.com | user      | password |
    Then A user "user" is created with the following info:
       | email          | username  | password |
       | user@email.com | user      | password |

  Scenario: User email is normalized
    Given I have the email "test@CAPT.COM"
    When I create a user with my email
    Then The user is registered with the email in lower case

  Scenario: Creating user without email raises ValueError
    When I create a user without providing an email
    Then An error is raised
    And The error is a ValueError

  Scenario: Creating a new super user
    When I create a super user using django support
    Then User is a superuser
    And User is a staff
