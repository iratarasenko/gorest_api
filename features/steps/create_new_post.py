from behave import *
import requests
import random


@given('A valid access token')
def step_impl(context):
    context.header = {'Authorization': 'Bearer HGFZjxWRKiD3ecuLxSj2O2yO_X_0zin8y8fz'}


@step('User exists in a database')
def step_impl(context):
    number = random.randint(1, 99999999)
    email = f"test_gorest_api{number}@gmail.com"

    user_data = {
        "first_name": "Test",
        "last_name": "Test",
        "gender": "male",
        "email": email,
    }
    response = requests.post('https://gorest.co.in/public-api/users', headers=context.header, json=user_data)
    context.user_response = response.json()
    context.user_response['_meta']['code'] == 200


@given('User provides a valid user id')
def step_impl(context):
    context.request_body = {"user_id": context.user_response['result']['id']}


@step('User provides some title as "{title}"')
def step_impl(context, title):
    context.request_body['title'] = title


@step('User provides some body as "{body}"')
def step_impl(context, body):
    context.request_body['body'] = body


@when('User submits the request to create a new post')
def step_impl(context):
    response = requests.post('https://gorest.co.in/public-api/posts', headers=context.header, json=context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('"200" status code is returned')
def step_impl(context):
    assert context.status_code == 200


@step('Post id is in the response body')
def step_impl(context):
    print(context.response_body)
    assert 'id' in context.response_body['result']


@step('Title "{title}" is in the response body')
def step_impl(context, title):
    assert context.response_body['result']['title'] == title


@step('Body "{body}" is in the response body')
def step_impl(context, body):
    assert context.response_body['result']['body'] == body
