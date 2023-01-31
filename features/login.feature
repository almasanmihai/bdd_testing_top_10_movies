Feature: Log In

  Background:
    Given Login: I navigate to login page

  @smoke
  Scenario:
    Then Login: I see navbar

  @regression
  Scenario Outline:
    When Login: I enter email "<email>"
    When Login: I enter password "<pswd>"
    When Login: I click on Log Me In
    Then Home: I see welcome back text
    Then Home: I see modified navbar
    Then Home: The url is "http://almasanmihai.pythonanywhere.com/"

    Examples:
      | email                  | pswd |
      | admin@email.com        | 123  |
      | almasanmihai@yahoo.com | 123  |
