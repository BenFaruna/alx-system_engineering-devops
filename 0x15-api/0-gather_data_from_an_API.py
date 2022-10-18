#!/usr/bin/python3
"""module for accessing API"""
import json
import requests
import sys


def get_data(user_id):
    """function gets user data from API and return user details and todos"""
    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    todo_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(user_id)).json()
    return user_data, todo_data


def main():
    """function gets all the necessary details to be displayed"""
    user_id = sys.argv[1]
    user_data, todo_data = get_data(user_id)

    tasks_num = len(todo_data)
    user_name = user_data.get('name')
    todo = ""

    # counts the number of task that was completed
    tasks_completed = 0
    for task in todo_data:
        if task.get('completed'):
            todo = todo + '\t ' + task.get('title') + '\n'
            tasks_completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, tasks_completed, tasks_num))
    print(todo, end='')


if __name__ == '__main__':
    main()
