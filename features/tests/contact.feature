Feature: Test scenarios for Contact us page

  Scenario: User can open the Contact us page
    Given Open Reelly login page
    When User logs in to the site
    And Settings option is clicked
    And Contact us option is clicked
    Then Verify 5 social media icons are displayed