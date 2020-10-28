# API test automation using BBD and data-driven testing approach

Project uses online open source REST API https://gorest.co.in/

## REST API https://gorest.co.in/ description

### Features tested
1. Create a user
2. Create a post
3. Find users with the corporate email

Note: Test "Find users with the corporate email" will fial because the endpoint https://gorest.co.in/public-api/users?email=@test.global' has been modified by the author. It doesn't except parameter in URI any more.

### Project set up
1. Download the project folder
2. Create a virtual environment in a main project folder
3. Install requirements.txt
4. Activate a virtual environment executing a command 'source venv/bin/activate' from the project folder
