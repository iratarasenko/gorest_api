Feature: Find users with a corporate email

    Background: Set up a user is database
      Given A valid access token
      And At least one user with "@test.global" in "<email>" field exists in a database

    Scenario: Find users with emails that contain @test.global
      Given Users that have "@test.global" in "<email>" field
      When I submit a request to find all users
      Then All users with "@test.global" in "<email>" field are shown