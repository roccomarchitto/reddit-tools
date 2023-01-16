#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""

# TODO - locked not working

__version__ = "0.4.0 PRE ALPHA"

import sys
import os

from dotenv import dotenv_values
from praw import Reddit

from .postfinder import RedditPostFinder
from .database import MongoWrapper
from .parser import Parser
from .analyzer import RedditAnalyzer


class AnalysisDriver:
    """
    TODO
    """

    @staticmethod
    def start_service(config: dict, user: str, query: str):
        # config is the parsed .env file dictionary
        mongo = MongoWrapper(config["MONGO_URL"], config["MONGO_DB_NAME"])

        # Start the service
        analyzer = RedditAnalyzer(mongo, user)

        if query == "subreddits":
            analyzer.get_subreddits()
        elif query == "titles":
            analyzer.get_titles()
        elif query == "scores":
            analyzer.get_scores()
        elif query == "locked":
            analyzer.get_locked()


class PostfinderDriver:
    """
    TODO
    """

    @staticmethod
    def start_service(config: dict, users_file: str):
        # config is the parsed .env file dictionary
        client_id = config["REDDIT_CLIENT_ID"]
        client_secret = config["REDDIT_CLIENT_SECRET"]
        user_agent = config["REDDIT_USER_AGENT"]
        reddit = PRAWConnector.connect(client_id, client_secret, user_agent)  # type: ignore
        mongo = MongoWrapper(config["MONGO_URL"], config["MONGO_DB_NAME"])  # type: ignore  TODO

        # Start the service
        # Note dependencies are injected in the RedditPostFinder constructor
        post_finder = RedditPostFinder(reddit, mongo)

        # For each user in the file, scrape posts, then add to processed_users.txt file
        # TODO .gitignore users file
        users = PostfinderDriver.file_to_usernames(users_file)

        # TODO parse as args instead of hardcode
        max_posts = 100  # Maximum number of posts per user to scrape
        max_users = 5  # Maximum number of users to scrape from the file
        for username in users[: max(max_users + 1, len(users) - 1)]:
            # Perform action, then move records to signify completion
            post_finder.find_user_posts(username, max_posts)
            # TODO: Check success
            with open("processed.log", "a") as f:
                f.write(username + "\n")
            with open("input.cfg", "r+") as f:
                lines = f.read().split()
                f.seek(0)
                f.write("\n".join(lines[1:]))
                f.truncate()

        # post_finder.find_user_posts("AudibleNod", 2)

    @staticmethod
    def file_to_usernames(filename: str) -> list:
        # Read file, split into list, strip each entry, then filter out empty strings
        with open(filename, "r") as f:
            users = list(
                filter(
                    lambda x: x,
                    list(map(lambda x: x.strip(), f.read().split("\n"))),
                )
            )
        return users


class PRAWConnector:
    @staticmethod
    def connect(client_id: str, client_secret: str, user_agent: str) -> Reddit:
        reddit = Reddit(
            client_id=client_id, client_secret=client_secret, user_agent=user_agent
        )
        return reddit


def main():
    # Load environment variables

    print(f"RedditTools\nVersion {__version__}")

    env_path = os.path.abspath(os.getcwd()) + "/.env"
    config = dotenv_values(env_path)

    arg_config = Parser.parse(sys.argv[1:])
    if "postfinder" in arg_config:
        # Postfinder service should be invoked
        users_file = arg_config["postfinder"]
        print("Calling postfinder on file", users_file)
        PostfinderDriver.start_service(config, users_file)
    if "analyzer" in arg_config:
        user, query = arg_config["analyzer"]
        # Analyzer service should be invoked
        print("Invoking analyzer on user", user, "with query", query)
        AnalysisDriver.start_service(config, user, query)

    # TODO: Drop duplicate posts in DB by ID; furthermore, if this is detected in
    #       a run with a large number of tasks, abort the run
