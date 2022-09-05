Feature: Login page
  - Tests for functionality on the login page

  Scenario: I am able to log in
    When I enter my username
    And I enter my password
    And I click the Log In button
    Then I am directed to the "/home" page

  Scenario: Unable to log in with bad password
    When I enter my username
    And I enter the password "ThisIsABadPassword1"
    And I click the Log In button
    Then an error appears that includes text "We didn't recognize that email and/or passwordzzz."
  
  Scenario: Navigate to password reset using Help link
    When I click the help link
    Then I am taken to the forgot password form

  Scenario: Navigate to password reset using Help link present in error message
    Given I enter my username
    And I enter the password "ThisIsABadPassword1"
    And I click the Log In button
    When I click the help link in the error message
    Then I am taken to the forgot password form

  Scenario: XSS attempt doesn't result in alert
    When I enter the username "<script>alert('UH OH!')</script>"
    And I enter my password
    And I click the Log In button
    Then an alert does not appear

