import multiprocessing
from datetime import datetime
from time import time

def my_func(i,result):
    result.put('calling myFunc from process n°: %s' % i + str(datetime.fromtimestamp(time())))
    for j in range(0, i):
       result.put('output from myFunc is :%s' % j  + str(datetime.fromtimestamp(time())))


def scenario_1():
    result = multiprocessing.Queue()
    for i in range(6):
        process = multiprocessing.Process(target=my_func, args=(i,result,))
        process.start()
        process.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_2():
    result = multiprocessing.Queue()
    processes = []
    for i in range(6):
        processes.append(multiprocessing.Process(target=my_func, args=(i,result,)))
        processes[-1].start()
    for process in processes:
        process.join()
    return [result.get() for _ in range(result.qsize())]



def scenario_3():
    result = multiprocessing.Queue()
    processes = []
    for i in range(6):
        processes.append(multiprocessing.Process(target=my_func, args=(i,result,)))
        processes[-1].start()
        if i <3:
            processes[-1].join()
            processes.pop(-1)
    for process in processes:
        process.join()
    return [result.get() for _ in range(result.qsize())]


