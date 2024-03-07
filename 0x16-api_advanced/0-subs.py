#!/usr/bin/python3
"""
Script returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns: number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "test_app:project (by Deantosh)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response_json = response.json()
        subscribers = response_json["data"]["subscribers"]
        return subscribers
    else:
        return 0
