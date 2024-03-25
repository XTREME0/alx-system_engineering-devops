#!/usr/bin/python3
"""get todo list using rest api export to json"""
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
    with open(f'{id}.json', 'a') as file:
        file.write('{"'+id+'": [')
        for i, task in enumerate(resp):
            title = task.get("title")
            status = task.get("completed")
            file.write(f'{{"task": "{title}", "competed": "{status}", "username": "{user}"}}')
            if i != len(resp) - 1:
                file.write(', ')
        file.write(']}')
