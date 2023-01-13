#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""


__version__ = "0.2.2 PRE ALPHA"

import sys
import os

from dotenv import dotenv_values
from praw import Reddit

from .postfinder import RedditPostFinder
from .database import MongoWrapper


class PRAWConnector:
    @staticmethod
    def connect(client_id: str, client_secret: str, user_agent: str):
        reddit = Reddit(
            client_id=client_id, client_secret=client_secret, user_agent=user_agent
        )
        print(reddit.read_only)
        return reddit


def main():
    # Load environment variables
    env_path = os.path.abspath(os.getcwd()) + "/.env"
    config = dotenv_values(env_path)
    print("CONFIG:", config, env_path, config["MONGO_URL"])

    client_id = config["REDDIT_CLIENT_ID"]
    client_secret = config["REDDIT_CLIENT_SECRET"]
    user_agent = config["REDDIT_USER_AGENT"]
    reddit = PRAWConnector.connect(client_id, client_secret, user_agent)  # type: ignore

    print(f"Version {__version__}")
    print(f"Args passed: {sys.argv[1:]}")
    mongo = MongoWrapper(config["MONGO_URL"], config["MONGO_DB_NAME"])  # type: ignore  TODO
    post_finder = RedditPostFinder(reddit, mongo)
    post_finder.find_user_posts("", 2)

    # TODO: Drop duplicate posts in DB by ID; furthermore, if this is detected in
    #       a run with a large number of tasks, abort the run
