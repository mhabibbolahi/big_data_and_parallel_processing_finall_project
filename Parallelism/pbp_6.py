import multiprocessing
import random
import time
from datetime import datetime


class Producer(multiprocessing.Process):
    def __init__(self, queue, result):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.result = result

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)

            self.result.put(
                f'Process Producer : item {item} appended to queue  {(self.name)}     {str(datetime.fromtimestamp(time.time()))}')
            time.sleep(1)
            self.result.put(f"The size of queue is {self.queue.qsize()}     {str(datetime.fromtimestamp(time.time()))}")


class Producer2(multiprocessing.Process):
    def __init__(self, queue, condition, result, ):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.condition = condition
        self.result = result

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            self.result.put(f"Process Producer : item {item} appended to queue {self.name}     {str(datetime.fromtimestamp(time.time()))}")
            self.condition.release()
            time.sleep(1)
            self.result.put(f"The size of queue is  {self.queue.qsize()}     {str(datetime.fromtimestamp(time.time()))}")


class Consumer(multiprocessing.Process):
    def __init__(self, queue, result, ):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.result = result

    def run(self):
        while True:
            if self.queue.empty():
                self.result.put(f"the queue is empty     {str(datetime.fromtimestamp(time.time()))}")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                self.result.put(f'Process Consumer : item {item} popped from by {self.name}     {str(datetime.fromtimestamp(time.time()))}')
                time.sleep(1)


class Consumer2(multiprocessing.Process):
    def __init__(self, queue, condition, result):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.condition = condition
        self.result = result

    def run(self):
        for i in range(10):
            self.condition.acquire()
            item = self.queue.get()
            self.result.put(f'Process Consumer : item {item} popped from by {self.name}     {str(datetime.fromtimestamp(time.time()))}')
            time.sleep(1)


def scenario_1():
    result = multiprocessing.Queue()
    queue = multiprocessing.Queue()
    for i in range(20):
        process_producer = Producer(queue, result)
        process_consumer = Consumer(queue, result)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()
        return [result.get() for _ in range(result.qsize())]


def scenario_2():
    result = multiprocessing.Queue()
    queue = multiprocessing.Queue()
    condition = multiprocessing.Semaphore(0)
    process_producer = Producer2(queue, condition, result)
    process_consumer = Consumer2(queue, condition, result)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
    return [result.get() for _ in range(result.qsize())]


def scenario_3():
    result = multiprocessing.Queue()
    queue = multiprocessing.Queue()
    process_producer = Producer(queue, result)
    process_consumer = Consumer(queue, result)
    process_producer.start()
    process_producer.join()
    process_consumer.start()
    process_consumer.join()
    return [result.get() for _ in range(result.qsize())]


