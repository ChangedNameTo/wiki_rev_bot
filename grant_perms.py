import praw

from datetime import datetime, timedelta

from praw.models import Message, Comment, Subreddit

from secrets import client_id, client_secret, user_agent, username, password

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

forbidden = ['automoderator-schedule']

for wikipage in reddit.subreddit('gatech').wiki:
    print(wikipage.name)
    if wikipage.name in forbidden:
        continue

    reddit.subreddit('gatech').wiki[wikipage.name].mod.add('bidong123')