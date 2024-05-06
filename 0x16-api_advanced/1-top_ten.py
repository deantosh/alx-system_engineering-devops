#!/usr/bin/python3
"""
Script queries the Reddit API and prints the titles of the first 10 hot posts\
 listed for a given subreddit.

Requirements:
  - Prototype: def top_ten(subreddit)
  - If not a valid subreddit, print None.

NOTE: Invalid subreddits may return a redirect to search results. Ensure that\
 you are not following redirects.
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}
    headers = {'User-Agent': 'windows:top_ten:v1.0.0 (by /u/deantosh)'}
    try:
        res = requests.get(url, params=params, headers=headers)
        res_dict = res.json()
        if 'data' in res_dict and 'children' in res_dict['data']:
            posts_data = res_dict["data"]["children"]
            for post in posts_data[1:]:
                title = post["data"]["title"]
                print(title)
        else:
            print(None)
    except Exception:
        print(None)
