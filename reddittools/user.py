#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


class User:
    """
    docstring TODO
    """

    def __init__(self):
        pass

    def test(self):
        pass


class UserPost:
    def __init__(self, post_attributes):

        # Private dictionary of post attributes
        self.__post = dict()

        # Valid post attributes list
        attribute_names = [
            "author",
            "id",
            "is_original_content",
            "name",
            "num_comments",
            "over_18",
            "score",
            "subreddit",
            "url",
            "selftext",
            "upvote_ratio",
        ]

        # For every valid attribute passed in, set the corresponding
        # entry in the private post attributes dictionary.
        # Note that the attributes dictionary is now immutable.
        for attribute in attribute_names:
            self.__post[attribute] = (
                post_attributes[attribute]
                if attribute in post_attributes
                else "DEFAULT"
            )

        # Add an ismedia category if needed
        if "selftext" in post_attributes:
            self.__post["ismedia"] = (
                True if post_attributes["selftext"] == "" else False
            )

    def get_post_dict(self):
        return self.__post


if __name__ == "__main__":
    pa = {"score": 5, "author": "testauth"}
    x = UserPost(pa)
    print(x.get_post_dict())
