#!/usr/bin/python3
"""get todo list using rest api"""
if __name__ == '__main__':
    import json
    import requests
    import sys
    id = sys.argv[1]
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/')
    resp = resp.json()
    user = resp.get("username")
    resp = requests.get('https://jsonplaceholder.typicode.com'
                        f'/users/{id}/todos/')
    resp = resp.json()
    with open(f'{id}.csv', 'a') as file:
        for task in resp:
            title = task.get("title")
            status = task.get("completed")
            file.write(f'"{id}","{user}","{status}","{title}"\n')
