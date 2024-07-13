import multiprocessing
import time
from datetime import datetime


def foo(result):
    result.put(f'Starting function' + str(datetime.fromtimestamp(time.time())))
    for i in range(0, 10):
        result.put(f'-->{i}' + str(datetime.fromtimestamp(time.time())))
        time.sleep(1)
        result.put('Finished function' + str(datetime.fromtimestamp(time.time())))


def scenario_1():
    result = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(result,))
    result.put('Process before execution:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    p.start()
    result.put('Process running:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    p.terminate()
    time.sleep(1)
    result.put('Process terminated:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    p.join()
    result.put('Process joined:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    return [result.get() for _ in range(result.qsize())]



def scenario_2():
    result = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(result,))
    result.put('Process before execution:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    p.start()
    while p.is_alive():
        time.sleep(1)
    result.put('Process is not alive' + str(datetime.fromtimestamp(time.time())))
    p.terminate()
    p.terminate()

    time.sleep(1)
    result.put('Process terminated:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    p.join()
    result.put('Process joined:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    return [result.get() for _ in range(result.qsize())]



def scenario_3():
    result = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(result,))
    result.put('Process before execution:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))

    p.start()
    result.put('Process started:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    time.sleep(5)
    p.terminate()
    result.put('Process is timeout' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    time.sleep(1)
    result.put('Process terminated:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    result.put('Process joined:' + str(p) + str(p.is_alive()) + str(datetime.fromtimestamp(time.time())))
    return [result.get() for _ in range(result.qsize())]
