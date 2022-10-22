#TODO: Start a thread. get that current time. chech if minute has incremented with one. if yes then check the hour again. if the old h - new h == 1 -> notify. start new thread with new h. ->> repeat


import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.warning("Time to stand up and take a walk")


def thread_pause(name):
    logging.info("Thread %s: pausing", name)
    time.sleep(10)

def main():
    format = "%(asctime)s: %(message)s" 
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Program started!")
    while True:
        x = threading.Thread(target=thread_function, args=(1,))
        logging.info("Main    : before running thread")
        x.start()
        x = threading.Thread(target=thread_pause, args=(1,))
        logging.info("Welcome back from the break!!")
        time.sleep(15)

        # break
        
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
if __name__ == "__main__":
    main()