#!/usr/bin/python3
"""module for accessing API"""
import csv
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

    username = user_data.get('username')

    with open('{}.csv'.format(user_id), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow((user_id, username,
                                task.get('completed'), task.get('title')))


if __name__ == '__main__':
    main()
