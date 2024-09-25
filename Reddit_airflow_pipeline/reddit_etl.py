import pandas as pd
import json
import praw
from datetime import datetime
import s3fs

reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME",
)

print(reddit.read_only)