#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .user import User, UserPost


class RedditPostFinder:
    def __init__(self, reddit, mongo):
        # reddit is the PRAW dependency injection (Reddit object)
        # mongo is the MongoDB dependency injection (MongoClient)
        self.reddit = reddit
        self.mongo = mongo
        print("Post finder invoked.")
        pass

    def find_user_posts(self, username: str, limit: int = 1) -> bool:
        """Scrape the max number of (~1000) new posts for a user and send to the database."""
        try:
            reddit_account = self.reddit.redditor(username)
            submissions = reddit_account.submissions.new(
                limit=limit
            )  # TODO limit magic number?
            user_posts = list()
            idx = 0
            for post in submissions:
                user_data = {
                    "author": post.author.name,
                    "id": post.id,
                    "is_original_content": post.is_original_content,
                    "title": post.title,
                    "num_comments": post.num_comments,
                    "over_18": post.over_18,
                    "score": post.score,
                    "subreddit": post.subreddit.display_name,
                    "url": post.url,
                    "selftext": post.selftext,
                    "upvote_ratio": post.upvote_ratio,
                    "permalink": post.permalink,
                }
                print(user_data)
                post_object = UserPost(user_data)
                user_posts.append(post_object)
                idx += 1

            print(*user_posts, sep="\n")
            print("SUBMITITNG POSTS TO DATABASE")
            for post in user_posts:
                self.mongo.submit_post(post)
            print("Complete.")

            return True
        except Exception as e:
            print("Error scraping user post:", e)
            return False
