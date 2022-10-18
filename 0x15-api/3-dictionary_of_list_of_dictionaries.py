#!/usr/bin/python3
"""module for accessing API"""
import json
import requests


def get_data(user_id):
    """function gets user data from API and return user details and todos"""
    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    todo_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user_id)).json()

    return user_data, todo_data


def main():
    """gets all the tasks of users and their username and save to a file"""
    user_dict = {}
    for user_id in range(1, 11):
        user_data, todo_data = get_data(user_id)

        username = user_data.get('username')
        user_dict[user_id] = []
        for task in todo_data:
            user_dict[user_id].append({
                                        'username': username,
                                        'task': task.get('title'),
                                        'completed': task.get('completed'),
                                      })

    with open('todo_all_employees.json'.format(user_id), 'w') as f:
        csv_writer = json.dump(user_dict, f)


if __name__ == '__main__':
    main()
