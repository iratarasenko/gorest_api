from behave import *
import requests
import random


@given('User has a valid access token')
def step_impl(context):
    context.header = {'Authorization': 'Bearer 0e063d9dee1adca4508755a41d99c37451675953bc1b1e61a26ec7a16f66e228'}


@when('I provide valid data to all required fields')
def step_impl(context):
    number = random.randint(1, 999999)
    email = f'test.gorest{number}@gmail.com'
    user_data = {
        "name": "Test",
        "gender": "Male",
        "email": email,
        "status": "Active"
    }
    context.new_user_data = user_data


@when('I provide invalid data to all required fields: already existing email')
def step_impl(context):
    user_data = {
        "name": "Test",
        "gender": "Male",
        "email": 'test02@gmail.com',
        "status": "Active"
    }
    context.new_user_data = user_data


@step('I submit the request to create a new user')
def step_impl(context):
    print(context.header)
    print(context.new_user_data)
    response = requests.post(
        'https://gorest.co.in/public-api/users',
        headers=context.header,
        json=context.new_user_data,
    )
    context.response_body = response.json()
    context.response_headers = response.headers
    print(context.response_body)
    print(context.response_headers)
    assert response.status_code == 200


@then('A new user is successfully created')
def step_impl(context):
    assert context.status_code == requests.codes.ok
    assert context.response_body['code'] == 201


@then('Error response code is returned')
def step_impl(context):
    assert context.status_code['code'] == 422


@step('Error is raised for email field')
def step_impl(context):
    assert context.response_body['data'][0]['field'] == 'email'
