#!/usr/bin/python3
""" module of the function top_ten """

import requests


def top_ten(subreddit):
    """
     Retrieve and print the titles of the top ten hot posts for a
     given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to
        retrieve the top ten hot posts.
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, headers=user_agent).json()

    i = 1
    for post in response.get('data', {}).get('children', []):
        if i > 10:
            break
        print(post.get('data').get('title'))
        i += 1
    else:
        print(None)
