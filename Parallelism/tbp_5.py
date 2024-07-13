import random
import threading
import time

result = []


class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)


class Box2:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)
            time.sleep(5)

    def remove(self):
        with self.lock:
            self.execute(-1)


class Box3:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)
            time.sleep(5)


def adder(box, items):
    result.append(f"N° {items} items to ADD ")
    while items:
        box.add()
        items -= 1
        result.append(f"ADDED one item -->{items} item to ADD ")


def remover(box, items):
    result.append(f"N° {items} items to REMOVE")
    while items:
        box.remove()
        items -= 1
        result.append(f"REMOVED one item -->{items} item to REMOVE")


def scenario_1():

    global result
    result = []
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return result


def scenario_2():

    global result
    result = []
    box = Box2()
    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return result


def scenario_3():

    global result
    result = []
    box = Box3()
    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return result


