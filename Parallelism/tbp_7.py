from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

runners = ['Huey', 'Dewey', 'Louie', 'Jan', 'Alex']
finish_line = Barrier(len(runners))
sh = 0

result =[]
def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    result.append(f' {name} reached the barrier at: {ctime()}')
    finish_line.wait()
    global sh
    sh += 1


def runner2():
    name = runners.pop()
    sleep(randrange(2, 5))
    result.append(f' {name} reached the barrier at: {ctime()}')
    global sh
    sh += 1


def scenario_1():

    global result
    result = []
    global sh
    runners_num = len(runners)
    result.append('START RACE!!!!')
    for i in range(runners_num):
        Thread(target=runner).start()
    while sh < (runners_num-1):
        sleep(1)
    result.append('Race over!')


def scenario_2():

    global result
    result = []
    result.append('START RACE!!!!')
    threads = []
    for i in range(len(runners)):
        threads.append(Thread(target=runner2))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append('Race over!')


def scenario_3():

    global result
    result = []
    # this output without Barrier
    result.append('START RACE!!!!')
    threads = []
    for i in range(len(runners)):
        threads.append(Thread(target=runner2))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append('Race over!')

