# Multithreading task

import threading
import logging
import time


class Async(threading.Thread):

    def __init__(self, delay, name):
        threading.Thread.__init__(self)  # initialize the thread
        self.delay = delay
        self.name = name

    def run(self):
        time.sleep(self.delay)
        logging.info("Performed the function in the background: " + self.name)


def main():
    logging.getLogger("").setLevel(logging.INFO)  # setting the logging level from which we want to receive messages
    logging.info("Program start")

    thread1 = Async(1, "thread1")  # 1 because this is our delay - the waiting time for the program execution
    thread2 = Async(2, "thread2")
    thread3 = Async(0.5, "thread3")

    thread1.start()
    thread2.start()
    thread3.start()

    logging.info("Something is going on in the program")

    thread3.join()
    thread2.join()
    thread1.join()

    logging.info("Thread ended")


# the fastest is thread 3 because it has the shortest waiting time
# then thread 1 and finally thread 2

if __name__ == '__main__':
    main()
