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

    @logger
    def get_scores(self):
        """
        Return a list of the most recent post scores for the specified user.
        """
        posts = self.mongo.get_post(self.user)
        posts_arr = [str(post["score"]) for post in posts]
        # By default, sort by occurrence
        return posts_arr

    @logger
    def get_locked(self):
        """
        Return a list of the most recent subreddits for the specified user.
        """
        posts = self.mongo.get_post(self.user)
        posts_arr = [str(post["locked"]) for post in posts]
        amt_locked = str(posts_arr.count("True"))
        posts_arr.insert(0, str(float(int(amt_locked) / len(posts_arr))))
        # First entry is percent locked
        return posts_arr

    @logger
    def get_titles(self):
        """
        Return a list of the most recent subreddits for the specified user.
        """
        posts = self.mongo.get_post(self.user)
        posts_arr = [post["title"] for post in posts]
        # By default, sort by recent occurrence
        return posts_arr
