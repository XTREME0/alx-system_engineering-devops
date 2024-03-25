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
        for task in resp:
            json.dump({id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user
                }]}, file)
