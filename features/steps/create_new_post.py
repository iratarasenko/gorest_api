from behave import *
import requests


@given('I provide valid data to all required post fields')
def step_impl(context):
    post = {
        "user_id": context.users[0]['id'],
        "title": "Test title",
        "body": "Test body"
    }
    context.new_post = post


@when('I submit the request to create a new post')
def step_impl(context):
    response = requests.post(
        'https://gorest.co.in/public-api/posts',
        headers=context.header,
        json=context.new_post,
    )
    context.response_body = response.json()
    context.status_code = response.status_code


@then('A new post is successfully created')
def step_impl(context):
    assert context.status_code == 200
    assert context.response_body['code'] == 201
