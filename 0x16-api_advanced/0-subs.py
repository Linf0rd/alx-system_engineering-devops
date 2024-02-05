#!/usr/bin/python3
"""
0-subs module
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If an invalid subreddit is given, the function returns 0.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return 0
        else:
            print(f"HTTP Error: {e}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
