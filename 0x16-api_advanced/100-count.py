#!/usr/bin/python3
""" module of the function count_words """

import requests
import re


def count_words(subreddit, word_list, hot_dict={}, after=""):
    """
    Count occurrences of words in a subreddit's hot posts.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to search for.
        hot_dict (dict, optional): A dictionary to store word counts.
                                  Defaults to {}.
        after (str, optional): A Reddit post identifier for pagination.
                              Defaults to "".
    """
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"after": after}, headers=user_agent)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            hot_dict = sorted(hot_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, occurence in hot_dict:
                print('{}: {}'.format(word, occurence))
            return
        for post in response.json().get("data").get("children"):
            for word in word_list:
                pattern = re.escape(word.lower())
                target = post.get('data').get('title').lower()
                if bool(re.search(r'\b{}\b'.format(pattern), target)):
                    hot_dict[word.lower()] = hot_dict.get(word, 0) + 1
        return count_words(subreddit, word_list, hot_dict, after)
