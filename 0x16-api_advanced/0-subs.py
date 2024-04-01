#!/usr/bin/python3
"""
a function that returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of not active users, total subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    # Set a custom User-Agent to avoid rate limiting

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

