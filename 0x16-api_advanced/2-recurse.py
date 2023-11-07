#!/usr/bin/python3
""" module of the function recurse """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively retrieve and append the titles of the top hot posts for
    a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to retrieve
                        the top hot posts.
        hot_list (list): A list to which the post titles are appended.
                        Used for recursive calls.
        after (str): The Reddit API 'after' parameter, which is used to
                    navigate through pagination.

    Returns:
        list: A list containing the titles of the top hot posts from the
            specified subreddit.
            Returns an empty list if the subreddit is not found.
    """
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"after": after}, headers=user_agent)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            return hot_list
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
