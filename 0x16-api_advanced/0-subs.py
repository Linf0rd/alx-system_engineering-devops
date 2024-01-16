#!/usr/bin/python3
"""
This module provides a function to query the Reddit API,
for the number of subscribers of a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number,
    of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit,
        or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Subber/0.1 by CtrlWorldWide"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
