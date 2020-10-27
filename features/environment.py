import requests
import json


def before_all(context):
    context.header = {'Authorization': 'Bearer {'token received after authorization on https://gorest.co.in/'}
    context.users = []

    f = open('features/steps/users.json')
    users = json.loads(f.read())
    for user in users:
        response = requests.post(
            'https://gorest.co.in/public-api/users',
            headers=context.header,
            json=user,
        )
        created_user = response.json()['data']
        context.users.append(created_user)
    print(context.users)


def after_all(context):
    for user in context.users:
        user_id = user['id']
        response = requests.delete(
            f'https://gorest.co.in/public-api/users/{user_id}',
            headers=context.header,
        )
        print(response.json())
