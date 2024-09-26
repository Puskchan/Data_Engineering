import pandas as pd
import json
import praw
from datetime import datetime
import s3fs
from env import CLIENT_SECRET, CLIENT_ID, USERAGENT


reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USERAGENT,
)
posts = []
for submission in reddit.subreddit('developers').hot(limit=100):
    post = {
        "title": submission.title,
        "author": submission.author,
        "score": submission.score
    }
    posts.append(post)


df = pd.DataFrame(posts)
df.to_csv("reddit_posts")