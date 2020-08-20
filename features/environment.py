import requests
import json


def before_all(context):
    context.header = {'Authorization': 'Bearer 0e063d9dee1adca4508755a41d99c37451675953bc1b1e61a26ec7a16f66e228'}
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
