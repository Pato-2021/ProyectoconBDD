Feature: login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Background:
    Given the Store webPage

  Scenario: login in Store correctly
    When complete "PatoM" and "Automatizacion"
    Then my account page is displayed

  Scenario: Complete user and password around
    When complete "aaaaa" and "aaaaa"
    Then the error "Error: Incorrect login or password provided." is displayed