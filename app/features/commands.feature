Feature: Command feature tests

  Scenario: Wait for db should succeed if the DB is up
    Given The DB works on the "1" try
    When I call the command "wait_for_db"
    Then The DB is called exactly "1" times

  Scenario: Wait for DB should fail every time django has an operational error
    Given The function sleep is mocked
    And The DB works on the "6" try
    When I call the command "wait_for_db"
    Then The DB is called exactly "6" times

