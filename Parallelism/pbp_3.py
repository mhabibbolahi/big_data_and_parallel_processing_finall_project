import multiprocessing
import time
from datetime import datetime


def foo(result):
    name = multiprocessing.current_process().name
    result.put(f"Starting {name}    ." + str(datetime.fromtimestamp(time.time())))
    if name == 'background_process':
        for i in range(0, 5):
            # result.put(f'---> {i}   ' + str(datetime.fromtimestamp(time.time())))
            time.sleep(1)
    else:
        for i in range(5, 10):
            result.put(f'---> {i}   .' + str(datetime.fromtimestamp(time.time())))
            time.sleep(1)
            result.put(f"Exiting {name}     ." + str(datetime.fromtimestamp(time.time())))


def scenario_1():
    result = multiprocessing.Queue()
    background_process = multiprocessing.Process(name='background_process', target=foo, args=(result,))
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo, args=(result,))
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
    background_process.join()
    NO_background_process.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_2():
    result = multiprocessing.Queue()
    background_process = multiprocessing.Process(name='background_process', target=foo, args=(result,))
    background_process.daemon = False
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo, args=(result,))
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()
    background_process.join()
    NO_background_process.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_3():
    result = multiprocessing.Queue()
    background_process = multiprocessing.Process(name='background_process', target=foo, args=(result,))
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo, args=(result,))
    NO_background_process.daemon = True
    background_process.start()
    NO_background_process.start()
    background_process.join()
    NO_background_process.join()
    return [result.get() for _ in range(result.qsize())]
