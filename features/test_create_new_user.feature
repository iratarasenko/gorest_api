Feature: Create a user

  Background: Set up a user is database
    Given A valid access token

  Scenario Outline: Create a user using valid data and valid access token
    Given User has a first name as "<first_name>"
    And User has a last name as "<last_name>"
    And User has a gender info as "<gender>"
    And User has an email as "<email>"
    When I submit the request to create a new user
    Then "200" status code is returned
    And 200 response code is returned in response body meta
    And First name "<first_name>" is in the response body
    And Last name "<last_name>" is in the response body
    And Gender is "<gender>" is in the response body
    And Email "<email>" is in the response body
    And Id is in the response body


    Examples: test data positive flow
    | first_name | last_name | gender | email |
    | Karen | Smith | female | test29.email@gmail.com |
    #| John | Lincoln | male | test21.email@gmail.com |


  Scenario Outline: Create a user with an existing email
    Given User has a first name as "<first_name>"
    And User has a last name as "<last_name>"
    And User has a gender info as "<gender>"
    And User has an email as "<email>" that already exists in the data base
    When I submit the request to create a new user
    Then 422 response code is returned in the response body
    And Error message "Email "<email>" has already been taken." is returned in the response body


    Examples:
      | first_name | last_name | gender | email |
      | Jim | Forester | male | test18.email@gmail.com |


  Scenario Outline: Create a user when the mandatory field email is empty
    Given User has a first name as "<first_name>"
    And User has a last name as "<last_name>"
    And User has a gender info as "<gender>"
    And User does not have an email
    When I submit the request to create a new user
    Then 422 response code is returned in the response body
    And Error message "Email cannot be blank." is returned the response body

    Examples:
      | first_name | last_name | gender | email |
      | Jared | Jones | male |  |
