#!/usr/bin/python3
"""get subscribers count"""
import requests


def number_of_subscribers(subreddit):

    endpoint = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    r = requests.get(endpoint)
    if r.status_code == 200 and 'subscribers' in r.json().get('data'):
        return r.json().get('data').get('subscribers')
    return 0
