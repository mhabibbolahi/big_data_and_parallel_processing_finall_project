import logging
import random
import threading
import time
from datetime import datetime

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %\
# (message)s'
# logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
semaphore = threading.Semaphore(0)
Item = []
result = []


def consumer():
    result.append(f'{datetime.fromtimestamp(time.time())},  {threading.current_thread().name}, Consumer is waiting')
    semaphore.acquire()
    logging.info(
        f'{datetime.fromtimestamp(time.time())},  {threading.current_thread().name},  Consumer notify: item number {(Item.pop(-1), Item)}')


def producer():
    item = random.randint(0, 1000)
    Item.append(item)
    time.sleep(3)
    logging.info(f'{datetime.fromtimestamp(time.time())},  {threading.current_thread().name},   Producer notify: item number {item}')
    semaphore.release()


def scenario_1():
    global result
    result = []
    for i in range(10):
        threading.Thread(target=consumer).start()
        threading.Thread(target=producer).start()
    return result


def scenario_2():
    global result
    result = []
    for i in range(10):
        threading.Thread(target=producer).start()
    for i in range(10):
        threading.Thread(target=consumer).start()
    return result


def scenario_3():
    global result
    result = []
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=consumer))
        threads.append(threading.Thread(target=producer))
        threads[-1].start()
        threads[-2].start()
        threads[-1].join()
        threads[-2].join()
    return result


print(scenario_1())
