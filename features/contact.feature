Feature: Contact page

  Background:
    Given Contact: I navigate on contact page

  @smoke
  Scenario:
    Then Contact: I see email link

  @smoke
  Scenario:
    Then Contact: I see navbar