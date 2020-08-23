Feature: Create a user


  Scenario: Create a user using valid data
    When I provide valid data to all required fields
    And I submit the request to create a new user
    Then A new user is successfully created


  Scenario: Create a user with an existing email
    When I provide invalid data to all required fields: already existing email
    And I submit the request to create a new user
    Then Error response code is returned
    And Error is raised for email field


  Scenario: Create a user when the mandatory field email is empty
    When I provide invalid data to all required fields: no email
    And I submit the request to create a new user
    Then Error response code is returned
    And Error is raised for email field
