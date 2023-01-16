#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Parse command line arguments.
TODO
"""

from argparse import ArgumentParser


class Parser:
    @staticmethod
    def parse(arglist: list) -> dict:
        parser = ArgumentParser(prog="Program name")
        # Postfinder arguments
        parser.add_argument(
            "-p",
            "--postfinder",
            nargs="?",
            const="default_postfinder",
            help="specify postfinder functionality along with file of usernames",
        )
        # Analyzer arguments
        parser.add_argument(
            "-a",
            "--analyzer",
            nargs="*",
            default="default_analyzer",
            help="analyze a scraped user's posts",
        )

        # Parse the arguments
        args = parser.parse_args(arglist)

        argdict = dict()
        Parser.parse_postfinder(args, argdict)
        Parser.parse_analyzer(args, argdict)
        return argdict

    @staticmethod
    def parse_analyzer(args, argdict: dict) -> None:
        """
        The analyzer performs queries against a specified user's posts in the database.
        The queries generate CSV reports for further analysis.
        The possible queries are:
            subreddits list (subreddits)
            post scores (scores)
            locked percentage (locked)
            titles list (titles)
        """
        if (
            args.analyzer and args.analyzer != "default_analyzer"
        ):  # TODO make this better
            valid_queries = ["subreddits", "scores", "locked", "titles", "summary"]
            if len(args.analyzer) != 2:
                raise Exception("Analyzer arguments are incorrect.")
            elif args.analyzer[1] not in valid_queries:
                raise Exception("Analyzer query not valid.")
            else:
                argdict["analyzer"] = (
                    args.analyzer[0],
                    args.analyzer[1],
                )  # username, query

    @staticmethod
    def parse_postfinder(args, argdict: dict) -> None:  # TODO type?
        """
        TODO
        """
        if args.postfinder and args.postfinder != "default_postfinder":
            users_file = ""
            users_file = args.postfinder

            # Put the results into a dictionary and return it
            argdict["postfinder"] = users_file
