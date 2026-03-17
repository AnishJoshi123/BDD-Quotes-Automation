Feature: Quotes website

Scenario: Open website
    Given user opens quotes website
    Then user should see the homepage

Scenario: Login with valid credentials
    Given user opens quotes website
    When user clicks on login button
    And user enters username
    And user enters password
    And user clicks submit button
    Then user should be logged in successfully

Scenario: Logout after login
    Given user opens quotes website
    When user clicks on login button
    And user enters username
    And user enters password
    And user clicks submit button
    And user clicks logout button
    Then user should be logged out successfully

Scenario: Click on Change tag
    Given user opens quotes website
    When user clicks on Change tag
    Then user should see Change tag quotes

Scenario: Click on Deepthought tag
    Given user opens quotes website
    When user clicks on Deepthought tag
   

Scenario: Click on Thinking tag
    Given user opens quotes website
    When user clicks on Thinking tag
    Then user should see Thinking tag quotes

Scenario: Click on World tag
    Given user opens quotes website
    When user clicks on World tag
    Then user should see World tag quotes

Scenario: Navigate through all pages
    Given user opens quotes website
    When user clicks next button until last page
    Then user should reach the last page







    








