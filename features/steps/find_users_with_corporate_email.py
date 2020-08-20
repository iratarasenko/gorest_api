from behave import *
import requests


@when('I submit a request to find all users')
def step_impl(context):
    response = requests.get('https://gorest.co.in/public-api/users?email=@test.global')
    context.response_body = response.json()
    context.status_code = response.status_code
    assert context.status_code == requests.codes.ok


@then('All users with "@test.global" in "{email}" field are shown')
def step_impl(context, email):
    pass
