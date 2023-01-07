#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""


__version__ = "0.2.1 PRE ALPHA"

import sys
import os


from dotenv import dotenv_values


from . import m
from .postfinder import RedditPostFinder


def main():
    # Load environment variables
    env_path = os.path.abspath(os.getcwd()) + "/.env"
    config = dotenv_values(env_path)
    print("CONFIG:", config, env_path, config["MONGO_URL"])

    print(f"Version {__version__}")
    print(f"Args passed: {sys.argv[1:]}")
    post_finder = RedditPostFinder()
