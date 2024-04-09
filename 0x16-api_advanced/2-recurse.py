#!/usr/bin/python3
"""recursive function using api"""
import requests


def recurse(subreddit, hot_list=[], after="", c=0):
    """return all titles"""

    endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        r = requests.get(endpoint, headers={'user-Agent': 'agent47'},
                         params={"after": after, "count": c},
                         allow_redirects=False)
    except Exception:
        return None
    if r.status_code >= 400:
        return None

    data = r.json().get('data')
    after = data.get('after')
    for i in data.get('children'):
        hot_list.append(i.get('data').get('title'))
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after, data.get('dist'))
