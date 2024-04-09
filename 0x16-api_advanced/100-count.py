#!/usr/bin/python3
"""get t and print sorted count"""


def count_words(subreddit, word_list, after=None, c={}):
    """count function"""
    import requests

    inf = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "agent-47"},
                       params={"after": after},
                       allow_redirects=False)
    if inf.status_code != 200:
        return None

    info = inf.json()

    hl = [child.get("data").get("title")
          for child in info
          .get("data")
          .get("children")]
    if not hl:
        return None

    word_list = list(dict.fromkeys(word_list))

    if c == {}:
        for word in word_list:
            c[word] = 0

    for t in hl:
        w = t.split(' ')
        for word in word_list:
            for s_word in w:
                if s_word.lower() == word.lower():
                    c[word] += 1

    if not info.get("data").get("after"):
        sc = sorted(c.items(), key=lambda kv: kv[0])
        sc = sorted(c.items(), key=lambda kv: kv[1], reverse=True)
        for key, value in sc:
            if value != 0:
                print('{}: {}'.format(key, value))
    else:
        return count_words(subreddit, word_list,
                           info.get("data").get("after"), c)
