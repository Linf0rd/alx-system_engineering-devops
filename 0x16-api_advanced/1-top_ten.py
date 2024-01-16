#!/usr/bin/python3
"""
This module provides a function to query the Reddit API,
for the top 10 hot posts of a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API to retrieve and print the,
    titles of the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "TopTen/0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)
    else:
        print(None)
