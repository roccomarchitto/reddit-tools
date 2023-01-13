#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""

from abc import ABC, abstractmethod
from pymongo import MongoClient
from .user import User, UserPost


class DatabaseWrapper(ABC):
    """
    TODO
    """

    @abstractmethod
    def __init__(self):
        """
        TODO
        """
        pass

    @abstractmethod
    def connect(self):
        """
        TODO
        """
        pass

    @abstractmethod
    def submit_post(self):
        """
        TODO
        """
        pass

    @abstractmethod
    def submit_posts(self):
        """
        TODO
        """
        pass

    @abstractmethod
    def get_posts(self):
        """
        TODO
        """
        pass

    @abstractmethod
    def get_post(self):
        """
        TODO
        """
        pass


# TODO - singleton?
class MongoWrapper(DatabaseWrapper):
    def __init__(self, mongo_url: str, mongo_db_name: str) -> None:
        # Get a connection to the MongoDB database and select the collection
        self.mongo_url = mongo_url
        self.client = self.connect()
        self.db = self.client[mongo_db_name]
        self.collection = self.db["users"]

        # pa = {"author": "MOO", "score": 8}
        # u = UserPost(pa)
        # print("X:", self.submit_post(u))
        # print(self.get_posts()[-3:])

    def connect(self) -> MongoClient:
        client = MongoClient(self.mongo_url, serverSelectionTimeoutMS=5000)
        client.server_info()  # Raise an exception if the connection times out
        return client

    def submit_user(self) -> bool:
        # Submit a new user (and its in-memory posts) to the database
        # NOTE: This is a destructive action
        return False

    def submit_post(self, post_object: UserPost) -> bool:
        """Destructure a UserPost object and append to the user's database entry"""

        post_data = post_object.get_post_dict()
        username = post_data["author"]

        # If the user doesn't exist, create it
        user_dict = self.collection.find_one({"name": username})
        print(user_dict)
        if not user_dict:
            user_starter = {"name": username, "posts": []}
            self.collection.insert_one(user_starter)

        # Use the $push operator to append to the 'users' array
        newval = {"$push": {"posts": post_data}}
        update_status = self.collection.update_one({"name": username}, newval)
        # Ensure 1) at least one field was matched, and 2) the matched field was updated
        if (
            update_status.matched_count > 0
            and update_status.matched_count == update_status.modified_count
        ):
            return True  # Update succeeded
        else:
            return False

    # TODO typehint List[User]
    def get_posts(self):
        posts = [post for post in self.collection.find({})]
        return posts

    # TODO typehint
    def get_post(self, username: str):
        user_dict = self.collection.find_one({"name": username})
        return user_dict["posts"]  # type: ignore (Pylance suppression)

    def submit_posts(self):
        pass
