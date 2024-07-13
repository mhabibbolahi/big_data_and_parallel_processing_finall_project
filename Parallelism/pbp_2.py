import multiprocessing
import time
from datetime import datetime


def myFunc(Result):

    name = multiprocessing.current_process().name

    Result.put(f"Starting process name = {name} " + str(datetime.fromtimestamp(time.time())))
    time.sleep(3)
    Result.put(f"Exiting process name = {name}"+ str(datetime.fromtimestamp(time.time())))


def myFunc2(Result):

    name = multiprocessing.current_process().name
    Result.put(f"Starting process name = {name}"+ str(datetime.fromtimestamp(time.time())))
    Result.put(f"Exiting process name = {name}"+ str(datetime.fromtimestamp(time.time())))



def scenario_1():
    Result = multiprocessing.Queue()

    process_with_name = multiprocessing.Process(name='myFunc process', target=myFunc, args=(Result,))
    process_with_default_name = multiprocessing.Process(target=myFunc,args=(Result,))
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
    return [Result.get() for _ in range(Result.qsize())]


def scenario_2():
    Result = multiprocessing.Queue()
    process_with_name = multiprocessing.Process(name='myFunc process', target=myFunc,args=(Result,))
    process_with_default_name = multiprocessing.Process(target=myFunc,args=(Result,))
    process_with_name.start()
    process_with_name.join()
    process_with_default_name.start()
    process_with_default_name.join()
    return [Result.get() for _ in range(Result.qsize())]



def scenario_3():
    Result = multiprocessing.Queue()

    process_with_name = multiprocessing.Process(name='myFunc2 process', target=myFunc2,args=(Result,))
    process_with_default_name = multiprocessing.Process(target=myFunc2,args=(Result,))
    process_with_name.start()
    process_with_default_name.start()
    process_with_name.join()
    process_with_default_name.join()
    return [Result.get() for _ in range(Result.qsize())]

