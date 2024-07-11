import multiprocessing
import time
from datetime import datetime

class MyProcess(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        self.queue.put(f'called run method by {  self.name}    .' + str(datetime.fromtimestamp(time.time())))


def scenario_1():
    result = multiprocessing.Queue()
    for i in range(10):
        process = MyProcess(result)
        process.start()
        process.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_2():
    result = multiprocessing.Queue()
    processes = []
    for i in range(10):
        process = MyProcess(result)
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_3():
    result = multiprocessing.Queue()
    processes = []
    for i in range(10):
        process = MyProcess(result)
        process.start()
        if i < 5:
            process.join()
        else:
            processes.append(process)
    for process in processes:
        process.join()
    return [result.get() for _ in range(result.qsize())]


if __name__ == '__main__':
    print(scenario_3())
