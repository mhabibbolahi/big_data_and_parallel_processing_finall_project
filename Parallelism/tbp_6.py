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
    result.append(
        f'{datetime.fromtimestamp(time.time())},  {threading.current_thread().name},  Consumer notify: item number {(Item.pop(-1), Item)}')


def producer():
    item = random.randint(0, 1000)
    Item.append(item)
    time.sleep(3)
    result.append(f'{datetime.fromtimestamp(time.time())},  {threading.current_thread().name},   Producer notify: item number {item}')
    semaphore.release()


def scenario_1():
    global result
    result = []
    t1 = []
    t2 = []
    for i in range(10):
        t1.append(threading.Thread(target=consumer))
        t2.append(threading.Thread(target=producer))
        t1[-1].start()
        t2[-1].start()
    for i in range(10):
        t1[i].join()
        t2[i].join()
    return result


def scenario_2():
    global result
    result = []
    t1 = []
    t2 = []
    for i in range(10):
        t2.append(threading.Thread(target=producer))
        t2[-1].start()

    for i in range(10):
        t1.append(threading.Thread(target=consumer))
        t1[-1].start()
    for i in range(10):
        t1[i].join()
        t2[i].join()

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
