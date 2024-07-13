import threading
import time
import os
from threading import Thread
from random import randint
# Lock Definition
threadLock = threading.Lock()
result = []
class my_thread_class(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        threadLock.acquire()
        result.append(f"---> {self.name} running, belonging to process ID {str(os.getpid())}")
        time.sleep(self.duration)
        result.append(f"---> {self.name} over")
        threadLock.release()


class my_thread_class2(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        result.append(f"---> {self.name} running, belonging to process ID {str(os.getpid())}")
        threadLock.acquire()
        time.sleep(self.duration)
        threadLock.release()
        result.append(f"---> {self.name} over")


class my_thread_class3(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        threadLock.acquire()
        result.append(f"---> {self.name} running, belonging to process ID {str(os.getpid())}")
        threadLock.release()
        time.sleep(self.duration)
        result.append(f"---> {self.name} over")



def scenario_1():

    global result
    result = []
    start_time = time.time()
    threads = []
    thread_names = ["Thread#1 ", "Thread#2 ", "Thread#3 ", "Thread#4 ", "Thread#5 ", "Thread#6 ", "Thread#7 ",
                    "Thread#8 ", "Thread#9 "]
    for thread_name in thread_names:
        threads.append(my_thread_class2(thread_name, randint(1, 5)))
        threads[-1].start()
    for thread in threads:
        thread.join()
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
        threads.append(my_thread_class(thread_name, randint(1, 5)))
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
        threads.append(my_thread_class3(thread_name, randint(1, 5)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append("End")
    result.append(f"--- {(time.time() - start_time)} seconds ---")
    return result

