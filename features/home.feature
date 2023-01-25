Feature: Home page

  Background:
    Given Home: I navigate on home page

  @smoke
  Scenario:
    Then Home: I see login link

  @smoke
  Scenario:
    Then Home: The title is "Top 10 movies"

  @smoke
  Scenario:
    Then Home: The title url "http://almasanmihai.pythonanywhere.com/"