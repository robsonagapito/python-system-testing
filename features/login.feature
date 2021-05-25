Feature: Login access

  Background:
    Given user would like to log in application

  @smoke
  Scenario: User valid and password invalid
    
    Given user informs login with value equal "robson" with id
      And user informs password with value equal "GFT"
    When user clicks on login button
    Then user should see fail page with "Fail Login!" message

  @smoke
  Scenario: User valid and password valid
    Given user informs login with value equal "robson" with id
      And user informs password with value equal "agapito"
    When user clicks on login button
    Then user should see ok page with "Success Login!" message

  @all
  Scenario Outline: User valid and password valid
    Given user informs login with value equal "<User>" with id
      And user informs password with value equal "<Password>"
    When user clicks on login button
    Then user should see page with "<Result>" message

    Examples:
      | User   | Password | Result         |
      | robson | GFT      | Fail Login!    |
      | GFT    | agapito  | Fail Login!    |
      | GFT    | GFT      | Fail Login!    |
      | robson | agapito  | Success Login! |