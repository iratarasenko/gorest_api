from behave import *
import requests


@given('User has a valid access token')
def step_impl(context):
    context.header = {'Authorization': 'Bearer HGFZjxWRKiD3ecuLxSj2O2yO_X_0zin8y8fz'}


@given('User has a first name as "{first_name}"')
def step_impl(context, first_name):
    context.request_body = {"first_name": first_name}


@step('User has a last name as "{last_name}"')
def step_impl(context, last_name):
    context.request_body['last_name'] = last_name


@step('User has a gender info as "{gender}"')
def step_impl(context, gender):
    context.request_body['gender'] = gender


@step('User has an email as "{email}"')
def step_impl(context, email):
    context.request_body['email'] = email


@step('User has an email as "{email}" that already exists in the data base')
def step_impl(context, email):
    context.request_body['email'] = email


@step('User does not have an email')
def step_impl(context):
    context.request_body['email'] = ''


@when('I submit the request to create a new user')
def step_impl(context):
    response = requests.post('https://gorest.co.in/public-api/users', headers=context.header, json=context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('"{status_code}" status code is returned')
def step_impl(context, status_code):
    assert context.status_code == int(status_code)


@step('First name "{first_name}" is in the response body')
def step_impl(context, first_name):
    assert context.response_body['result']['first_name'] == first_name


@step('Last name "{last_name}" is in the response body')
def step_impl(context, last_name):
    assert context.response_body['result']['last_name'] == last_name


@step('Gender is "{gender}" is in the response body')
def step_impl(context, gender):
    assert context.response_body['result']['gender'] == gender


@step('Email "{email}" is in the response body')
def step_impl(context, email):
    assert context.response_body['result']['email'] == email


@step('Id is in the response body')
def step_impl(context):
    assert 'id' in context.response_body['result']


@step('200 response code is returned in response body meta')
def step_impl(context):
    assert context.response_body['_meta']['code'] == 200


@then('422 response code is returned in the response body')
def step_impl(context):
    assert context.response_body['_meta']['code'] == 422


@step('Error message "Email "{email}" has already been taken." is returned in the response body')
def step_impl(context, email):
    print(context.response_body)
    print(type(context.response_body['result'][0]['message']))
    assert context.response_body['result'][0]['message'] == f'Email "{email}" has already been taken.'


@step('Error message "Email cannot be blank." is returned the response body')
def step_impl(context):
    assert context.response_body['result'][0]['message'] == 'Email cannot be blank.'
