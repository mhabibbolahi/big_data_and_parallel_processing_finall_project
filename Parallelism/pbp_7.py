import multiprocessing
from datetime import datetime
from multiprocessing import Barrier, Lock, Process
from time import time


def test_with_barrier(synchronizer, serializer,result):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        result.put(f"process {name} ----> {datetime.fromtimestamp(now)}")


def test_with_barrier2(synchronizer, serializer,result):
    name = multiprocessing.current_process().name
    synchronizer.acquire()
    now = time()
    with serializer:
        result.put(f"process {name} ----> {datetime.fromtimestamp(now)}")
def test_with_barrier3(synchronizer, serializer,result):
    name = multiprocessing.current_process().name
    synchronizer.release()
    now = time()
    with serializer:
        result.put(f"process {name} ----> {datetime.fromtimestamp(now)}")


def test_without_barrier(result):
    name = multiprocessing.current_process().name
    now = time()
    result.put(f"process {name} ----> {datetime.fromtimestamp(now)}")


def scenario_1():
    result = multiprocessing.Queue()
    synchronizer = Barrier(2)
    serializer = Lock()
    p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result))
    p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result))

    p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier, args=(result,))
    p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier, args=(result,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    return [result.get() for _ in range(result.qsize())]



def scenario_2():
    result = multiprocessing.Queue()
    #  semaphore replace barrier
    synchronizer = multiprocessing.Semaphore(2)
    serializer = Lock()

    p1 = Process(name='p1 - test_with_semaphore', target=test_with_barrier2, args=(synchronizer, serializer,result))
    p2 = Process(name='p2 - test_with_semaphore', target=test_with_barrier3, args=(synchronizer, serializer,result))
    p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier,args=(result,))
    p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier,args=(result,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    return [result.get() for _ in range(result.qsize())]



def scenario_3():
    result = multiprocessing.Queue()
    #  delete lock
    synchronizer = multiprocessing.Barrier(2)
    serializer = Lock()
    p1 = Process(name='p1 - test_with_barrier_and_without_lock', target=test_with_barrier, args=(synchronizer, serializer,result))
    p2 = Process(name='p2 - test_with_barrier_and_without_lock', target=test_with_barrier, args=(synchronizer, serializer,result))
    p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier,args=(result,))
    p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier,args=(result,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    return [result.get() for _ in range(result.qsize())]


