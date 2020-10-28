from behave import *
import requests


@given('At least one user whose email ends with "@test.global" exists in a database')
def step_impl(context):
    assert [user for user in context.users if user['email'].endswith('@test.global')]


@when('I submit a request to find all users')
def step_impl(context):
    response = requests.get('https://gorest.co.in/public-api/users?email=@test.global')
    context.response_body = response.json()
    context.status_code = response.status_code
    assert context.status_code == requests.codes.ok
    assert context.response_body['code'] == requests.codes.ok


@then('All users with "@test.global" in "<email>" field are shown')
def step_impl(context):
    emails_from_response = []
    user_emails = [user['email'] for user in context.response_body['data'] if user['email'].endswith('@test.global')]
    emails_from_response.append(user_emails)
    assert emails_from_response == context.users

