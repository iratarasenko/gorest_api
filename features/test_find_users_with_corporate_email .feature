Feature: Find users with a corporate email


    Scenario: Find users with emails that contain @test.global
      Given At least one user whose email ends with "@test.global" exists in a database
      When I submit a request to find all users
      Then All users with "@test.global" in "<email>" field are shown