import os
import praw
from time import sleep

# from app.Services.timestamp import getTimestamp
# import RedditBotAccount
from apptest.models import RedditBotAccount


def setupPraw():  # logger):
    # Find in DB Reddit Bot account with is_active=True
    redditBotAccount = RedditBotAccount.objects.filter(is_active=True).first()
    try:
        r = praw.Reddit(
            client_id=redditBotAccount.client_id,
            client_secret=redditBotAccount.client_secret,
            username=redditBotAccount.username,
            password=redditBotAccount.password,
            user_agent=redditBotAccount.user_agent,
        )
        msg = "OAuth session opened as /u/" + r.user.me().name
        print(msg)
        # logger.info(msg)
        return r
    except Exception as e:
        print("Error: " + str(e))


# print(getTimestamp() + "Error: " + str(e))
# logger.error("[SETUP ERROR:]")
# sleep(10)

# show post title with most stars
def showPostTitleWithMostStars(r):
    for submission in r.subreddit("all").hot(limit=10):
        print(submission.title)
        print(submission.score)
        print("\n")
