# TODO: Start a thread. get that current time. chech if minute has incremented with one. if yes then check the hour again. if the old h - new h == 1 -> notify. start new thread with new h. ->> repeat

import logging
import threading
import time
from plyer import notification
import peewee

def thread_break_start(name):
    # logging.info("Thread %s: starting", name)
    time.sleep(5)
    '''Pop up notification for starting the break'''
    notification.notify(
        title="Break Time!",
        message="You've sat for one hour. It's time for a ten min break!",

        # displaying time
        timeout=2
    )

def break_end():
    logging.info("Thread end")
    notification.notify(
        title="Break is over!",
        message="Welcome back from your break! See you in an hour",

        # displaying time
        timeout=2
    )


def thread_pause(name):
    logging.info("Thread %s: pausing", name)
    time.sleep(10)


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Program started!")

    k = 0
    while True:

        x = threading.Thread(target=thread_break_start, args=(1,))

        x.start()
        x = threading.Thread(target=thread_pause, args=(1,))

        if k != 0:
            break_end()            
        k += 1
        time.sleep(15)

        break

    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")


if __name__ == "__main__":
    main()
