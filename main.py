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

updated_recently = ""

yesterday = datetime.now() - timedelta(days = 1)

for wikipage in reddit.subreddit('gatech').wiki:
    page_rev_dt = datetime.fromtimestamp(wikipage.revision_date)

    if page_rev_dt > yesterday:
        updated_recently = updated_recently + "|" + wikipage.name + "|" + wikipage.revision_by.name + "|\n"

if(updated_recently):
    message_body = '''
|Page|Revisor|
|---|---|
{}
Contact the owner u/TehAlpacalypse if the bot is broken.'''.format(updated_recently)

    today = datetime.now().strftime('%m/%d/%y')

    subject_str = "Wiki Revisions for {}".format(today)

    reddit.subreddit('gatech').message(subject_str, message_body)