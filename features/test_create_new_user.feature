Feature: Create a user

  Scenario Outline: Create a user using valid data and valid access token
    Given User provides a valid access token
    And User provides a first name as "<first_name>"
    And User provides a last name as "<last_name>"
    And User provides a gender info as "<gender>"
    And User provides an email as "<email>"
    When User submits the request
    Then "200" status code is returned
    And First name "<first_name>" is in the response body
    And Last name "<last_name>" is in the response body
    And Gender is "<gender>" is in the response body
    And Email "<email>" is in the response body
    And Id is in the response body
    And 200 response code is returned in response body meta


    Examples: test data positive flow
    | first_name | last_name | gender | email |
    | Karen | Smith | female | test5.test5.email@gmail.com |
    | John | Lincoln | male | test6.test6.email@gmail.com |