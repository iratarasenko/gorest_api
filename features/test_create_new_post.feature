Feature: Create a post

  Background: Set up a user is database
    Given A valid access token
    And User exists in a database

  Scenario: Create a post using valid data, existing user and valid access token
    Given User provides a valid user id
    And User provides some title as "<title>"
    And User provides some body as "<body>"
    When User submits the request to create a new post
    Then "200" status code is returned
    And Post id is in the response body
    And Title "<title>" is in the response body
    And Body "<body>" is in the response body
    And 200 response code is returned in response body meta