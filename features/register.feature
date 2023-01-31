Feature: Register

  Background:
    Given Register: I navigate on register page

  @smoke
  Scenario:
    Then Register: I see navbar

  @smoke
  Scenario:
    Then Register: I see Register text heading