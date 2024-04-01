#!/usr/bin/python3
"""
Script queries the Reddit API and returns the number of subscribers\
 (not active users, total subscribers) for a given subreddit. If an\
 invalid subreddit is given, the function should return 0.

Requirements:
  - Prototype: def number_of_subscribers(subreddit)
  - If not a valid subreddit, return 0.

NOTE:
  - Invalid subreddits may return a redirect to search results.
  - Ensure that you are not following redirects.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'windows:subs:v1.0.0 (by /u/deantosh)'}

    try:
        res = requests.get(url, headers=headers)
        res_dict = res.json()
        if 'data' in res_dict and 'subscribers' in res_dict["data"]:
            num_subs = res_dict["data"]["subscribers"]
            return num_subs
        else:
            return 0
    except Exception:
        return 0
