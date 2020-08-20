Feature: Create a user

  Background: Authorization
    Given A valid access token


  Scenario: Create a user using valid data
    When I provide valid data to all required fields
    And I submit the request to create a new user
    Then A new user is successfully created
  @after_scenario


  Scenario: Create a user with an existing email
    When I provide invalid data to all required fields: already existing email
    And I submit the request to create a new user
    Then Error response code is returned
    And Error is raised for email field
  @after_scenario


  Scenario: Create a user when the mandatory field email is empty
    Given I provide invalid data to all required fields: no email
    When I submit the request to create a new user
    Then Error response code is returned
    And Error is raised for email field
