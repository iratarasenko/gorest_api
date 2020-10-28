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
2. Create a virtual environment in a main project folder: execute a command 'python3.8 -m venv venv' in the project main folder
3. Activate a virtual environment executing a command 'source venv/bin/activate' from the project folder
4. Install requirements.txt: execute 'pip install -r requirements.txt'

### Access token configuration
Before test execution go to https://gorest.co.in/ and generate an access token.
In environment.py insert a valid token to: 
```
context.header = {'Authorization': 'Bearer {'token received after authorization on https://gorest.co.in/'}
```
