#!/usr/bin/python3
"""
Script uses a recursive function that queries the Reddit API parses the\
title of all hot articles, and prints a sorted count of given keywords.

Requirements:
  - Prototype: def count_words(subreddit, word_list)
  Note: You may change the prototype, but it must be able to be called with
        just a subreddit supplied and a list of keywords. AKA you can add a
        counter or anything else, but the function must work without supplying
        a starting value in the main.
  - If word_list contains the same word (case-insensitive), the final count
    should be the sum of each duplicate (example below with java)
  - Results should be printed in descending order, by the count, and if the
    count is the same for separate keywords, they should then be sorted
    alphabetically (ascending, from A to Z).
  - Words with no matches should be skipped and not printed. Words must be
    printed in lowercase.
  - Results are based on the number of times a keyword appears, not titles it
    appears in. java java java counts as 3 separate occurrences of java.
  - To make life easier, java. or java! or java_ should not count as java
  - If no posts match or the subreddit is invalid, print nothing.
  NOTE: Invalid subreddits may return a redirect to search results. Ensure that
        you are NOT following redirects.
"""
import requests


def count_words(subreddit, word_list):
    """count the keyword in a subreddit title posts"""
    params = {'limit': 100}

    # create a dictionary -- 'keyword': count
    keyword_dict = {keyword.lower(): 0 for keyword in word_list}

    # recursive API call
    read_posts(subreddit, word_list, keyword_dict, params)


def read_posts(subreddit, word_list, keyword_dict={}, params={}):
    """read the hot posts from API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:count_script:v1.0.0 (by /u/deantosh)"}

    try:
        res = requests.get(
              url, headers=headers, params=params, allow_redirects=False)
        data = res.json()

        if 'data' in data and 'children' in data["data"]:
            after = data["data"]["after"]

            posts = data["data"]["children"]
            for post in posts:
                title = post["data"]["title"]
                for keyword in keyword_dict.keys():
                    num = count_keyword(title, keyword)
                    keyword_dict[keyword] += num

            if after is not None:
                params['after'] = after
                read_posts(subreddit, word_list, keyword_dict, params)
            else:
                # sort the keyword_dict using values in descending order
                # if same values sort alphabetically using the keys
                sorted_keyword_dict = dict(sorted(
                     keyword_dict.items(),
                     key=lambda item: (item[1], item[0].lower()),
                     reverse=True))
                for key, value in sorted_keyword_dict.items():
                    if value == 0:
                        continue
                    print(f"{key}: {value}")

    except Exception as e:
        pass


def count_keyword(post_title, keyword):
    """count the number of keyword in a post title"""
    word_list = post_title.split(" ")
    count = 0

    for word in word_list:
        # for case insensitive scenario
        if word.lower() == keyword.lower():
            count += 1
    return count
