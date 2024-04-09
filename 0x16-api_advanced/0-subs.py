#!/usr/bin/python3
"""get subscribers count"""
import requests


def number_of_subscribers(subreddit):

    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    r = requests.get(endpoint)
    print(r.status_code)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    return 0
