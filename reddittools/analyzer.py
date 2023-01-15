#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import Counter


def logger(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        with open("logger.out", "w") as f:
            for item in res:
                f.write(item + "\n")
        print("DONE")

    return wrapper


class RedditAnalyzer:
    def __init__(self, mongo, user: str):
        """
        TODO
        """
        self.mongo = mongo
        self.user = user
        print("Analyzer invoked on user", user)

    # TODO: Use decorators to save to csv

    @logger
    def get_subreddits(self):
        """
        Return a list of the most recent subreddits for the specified user.
        """
        posts = self.mongo.get_post(self.user)
        posts_arr = [post["subreddit"] for post in posts]
        # By default, sort by frequency
        return sorted(posts_arr, key=posts_arr.count, reverse=True)
