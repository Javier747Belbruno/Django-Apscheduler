# runapscheduler.py
import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from apptest.util import setupPraw, showPostTitleWithMostStars
import datetime
from time import sleep
from signal import SIGBREAK, signal, SIGTERM
import os
from apptest.models import MessageCount


def getTimestamp():
    dt = (
        str(datetime.datetime.now().month)
        + "/"
        + str(datetime.datetime.now().day)
        + " "
    )
    hr = (
        str(datetime.datetime.now().hour)
        if len(str(datetime.datetime.now().hour)) > 1
        else "0" + str(datetime.datetime.now().hour)
    )
    min = (
        str(datetime.datetime.now().minute)
        if len(str(datetime.datetime.now().minute)) > 1
        else "0" + str(datetime.datetime.now().minute)
    )
    t = "[" + hr + ":" + min + "] "
    return dt + t


def checkUnreadMessages(reddit):
    # Check for new mail
    count = 0
    for msg in reddit.inbox.unread(limit=None):
        # msg.mark_read()
        count = count + 1

        subrredit_string = msg.subject.strip()
    # persist message count
    try:
        MessageCount.objects.create(
            count=count,
            created_at=datetime.datetime.now(),
        )
    except Exception as e:
        print(getTimestamp() + "Error: " + str(e))
    return count


def loop(logger, reddit):
    # Every minute, check mail, create new threads, update all current threads
    running = True
    retries = 0
    while running:
        try:
            count = checkUnreadMessages(reddit)
            print(
                getTimestamp()
                + "Checked for new messages. "
                + str(count)
                + " messages found."
            )
            showPostTitleWithMostStars(reddit)
            retries = 0
            sleep(60)
        except KeyboardInterrupt:
            logger.warning("[MANUAL SHUTDOWN]")
            # Only for development purposes - allows you to stop the server by pressing Ctrl+C
            # Works on Windows, so I dont know if it works on Linux
            print(
                getTimestamp()
                + "[MANUAL SHUTDOWN] - PID "
                + str(os.getpid())
                + " is shut down. \n"
            )
            os.kill(os.getpid(), SIGBREAK)
            #################

            # Prod code
            # running = False

        except UnicodeDecodeError:
            retries += 1
            print(
                getTimestamp()
                + "UnicodeDecodeError, check log file [retries = "
                + str(retries)
                + "]"
            )
            logger.exception("[UNICODE ERROR:]")
            # flushMsgs()
        except UnicodeEncodeError:
            retries += 1
            print(
                getTimestamp()
                + "UnicodeEncodeError, check log file [retries = "
                + str(retries)
                + "]"
            )
            logger.exception("[UNICODE ERROR:]")
            # flushMsgs()
        except Exception:
            retries += 1
            print(
                getTimestamp()
                + "Unknown error, check log file [retries = "
                + str(retries)
                + "]"
            )
            logger.exception("[UNKNOWN ERROR:]")
            sleep(60)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        reddit = setupPraw()
        logger = logging.getLogger("loop")
        loop(logger, reddit)
