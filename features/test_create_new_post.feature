Feature: Create a post


  Scenario: Create a post using valid data, existing user and valid access token
    Given I provide valid data to all required post fields
    When I submit the request to create a new post
    Then A new post is successfully created
