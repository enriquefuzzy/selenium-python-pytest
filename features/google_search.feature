Feature: Google Search
  Scenario: Verify Dog results are displayed
    Given the user is on Google
    When the user searches for "Dogs"
    Then Dog results are displayed
