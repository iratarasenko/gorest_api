# API test automation using BBD and data-driven testing approach

Project uses online open source REST API https://gorest.co.in/

## REST API https://gorest.co.in/ description

### Features tested
1. Create a user
2. Create a post
3. Find users with the corporate email

Note: Test "Find users with the corporate email" will fial because the endpoint https://gorest.co.in/public-api/users?email=@test.global' has been modified by the author. It doesn't except parameter in URI any more.
