#!/usr/bin/python3
"""get subscribers count"""
import requests


def top_ten(subreddit):

    endpoint = "https://www.reddit.com/r/{}/hot.json?limit=10"\
              .format(subreddit)

    try:
        r = requests.get(endpoint, headers={'user-Agent': 'agent47'},
                         allow_redirects=False)
        if r.ok:
            r = r.json().get('data').get('children')
            for line in r:
                print(line.get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
