#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO
"""

from abc import ABC, abstractmethod
from pymongo import MongoClient


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
        for i in range(500):
            self.submit_post()
        print(self.get_posts()[-3:])

        # print(self.client.database_names())
        # for i in self.client.list_database_names():
        #    print(i)
        # print("\n")
        # for i in self.db.list_collection_names():
        #    print(i)
        # self.submit_post()

    def connect(self) -> MongoClient:
        client = MongoClient(self.mongo_url, serverSelectionTimeoutMS=5000)
        client.server_info()  # Raise an exception if the connection times out
        return client

    def submit_post(self) -> str:
        # Serialize a UserPost object and append to the user

        username = "sss"
        import random

        post_schema = {
            "title": "example title",
            "author": "sampleauthor",
            "upvotes": random.random() * 100000,
            "ex": "example",
            "url": "https://www.reddit.com",
            "ex2": 200,
        }
        # Use the $push operator to append to the 'users' array
        newval = {"$push": {"posts": post_schema}}
        self.collection.update_one({"name": username}, newval)

        # post = {"name": "squilliam", "posts": ["squanto", "squarbo"]}
        # post_id = self.collection.insert_one(post).inserted_id
        # print(post_id)
        # return post_id

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
