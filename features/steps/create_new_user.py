from behave import *
import requests
import random


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
        "email": context.users[0]['email'],
        "status": "Active"
    }
    context.new_user_data = user_data


@when('I provide invalid data to all required fields: no email')
def step_impl(context):
    user_data = {
        "name": "Test",
        "gender": "Male",
        "email": '',
        "status": "Active"
    }
    context.new_user_data = user_data


@step('I submit the request to create a new user')
def step_impl(context):
    response = requests.post(
        'https://gorest.co.in/public-api/users',
        headers=context.header,
        json=context.new_user_data,
    )
    context.response = response
    context.response_body = response.json()
    assert response.status_code == 200, context.response_body


@then('A new user is successfully created')
def step_impl(context):
    assert context.response.status_code == requests.codes.ok
    assert context.response_body['code'] == 201, context.response_body


@then('Error response code is returned')
def step_impl(context):
    assert context.response_body['code'] == 422, context.response_body


@step('Error is raised for email field')
def step_impl(context):
    assert context.response_body['data'][0]['field'] == 'email', context.response_body
