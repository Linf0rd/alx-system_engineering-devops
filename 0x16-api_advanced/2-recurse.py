#!/usr/bin/python3
"""
Module containing the recurse() function to recursively fetch,
hot articles from a subreddit using the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches hot articles from a subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store the,
        article titles. Defaults to [].
        after (str, optional): The pagination token for the,
        next page of results. Defaults to None.

    Returns:
        list: A list of article titles, or None if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Hotlist'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    data = response.json()
    children = data['data']['children']

    for child in children:
        title = child['data']['title']
        hot_list.append(title)

    if data['data']['after']:
        return recurse(subreddit, hot_list, data['data']['after'])

    return hot_list
