import os
import time
from random import randint
from threading import Thread

result = []


class my_thread_class(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        result.append(f"---> {self.name}  running, belonging to process ID {os.getpid()} ")
        time.sleep(self.duration)
        result.append(f"---> {self.name}  over")


def scenario_1():

    global result
    result = []
    start_time = time.time()
    threads = []
    thread_names = ["Thread#1 ", "Thread#2 ", "Thread#3 ", "Thread#4 ", "Thread#5 ", "Thread#6 ", "Thread#7 ",
                    "Thread#8 ", "Thread#9 "]
    for thread_name in thread_names:
        threads.append(my_thread_class(thread_name, randint(1, 10)))
        threads[-1].start()
        threads[-1].join()
    result.append("End")
    result.append(f"--- {(time.time() - start_time)} seconds ---")
    return result


def scenario_2():

    global result
    result = []
    start_time = time.time()
    threads = []
    thread_names = ["Thread#1 ", "Thread#2 ", "Thread#3 ", "Thread#4 ", "Thread#5 ", "Thread#6 ", "Thread#7 ",
                    "Thread#8 ", "Thread#9 "]
    for thread_name in thread_names:
        threads.append(my_thread_class(thread_name, randint(1, 10)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append("End")
    result.append(f"--- {(time.time() - start_time)} seconds ---")

    return result

def scenario_3():

    global result
    result = []
    start_time = time.time()
    threads = []
    thread_names = ["Thread#1 ", "Thread#2 ", "Thread#3 ", "Thread#4 ", "Thread#5 ", "Thread#6 ", "Thread#7 ",
                    "Thread#8 ", "Thread#9 "]
    for thread_name in thread_names:
        threads.append(my_thread_class(thread_name, randint(1, 10)))
        threads[-1].start()
        if thread_names.index(thread_name) == 3:
            for thread in threads:
                thread.join()
                threads.remove(thread)
    for thread in threads:
        thread.join()

    result.append("End")
    result.append(f"--- {(time.time() - start_time)} seconds ---")

    return result
