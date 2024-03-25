#!/usr/bin/python3
"""get todo list using rest api export to json"""
if __name__ == '__main__':
    import json
    import requests
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/')
    resp = resp.json()
    with open(f'todo_all_employees.json', 'a') as file:
        json.dump({
            user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
            } for task in requests.get('https://jsonplaceholder.typicode.com/'
                'todos/', params={"userId": user.get("id")}).json()]
            for user in resp}, file)
