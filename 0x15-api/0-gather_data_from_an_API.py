#!/usr/bin/python3
"""get todo list using rest api"""

import json
import requests
import sys
id = sys.argv[1]
tasks = []
resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/')
resp = resp.json()
name = resp["name"]
resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos/')
resp = resp.json()
done = 0
for task in resp:
    if (task["completed"]):
        tasks.append(task["title"])
        done += 1
print(f'Employee {name} is done with tasks({done}/20):')
for task in tasks:
    print(task)
