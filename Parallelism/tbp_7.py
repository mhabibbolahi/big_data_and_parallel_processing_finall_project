from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

runners = ['Huey', 'Dewey', 'Louie', 'Jan', 'Alex']

finish_line = Barrier(len(runners))
sh = 0

def runner(name):
    global result
    sleep(randrange(2, 5))
    result.append(f' {name} reached the barrier at: {ctime()}')
    finish_line.wait()
    global sh
    sh += 1


def runner2(name):
    global result , sh
    sleep(randrange(2, 5))
    result.append(f' {name} reached the barrier at: {ctime()}')
    global sh
    sh += 1


def scenario_1():
    global result , sh
    result = []
    threads = []
    runners_num = len(runners)
    result.append('START RACE!!!!')
    for runner_name in runners:
        threads.append(Thread(target=runner,args=(runner_name,)))
        threads[-1].start()
    while sh < (runners_num-1):
        sleep(1)
    for thread in threads:
        thread.join()
    result.append('Race over!')
    return result


def scenario_2():
    global result
    result = []
    result.append('START RACE!!!!')
    threads = []
    for runner_name in runners:
        threads.append(Thread(target=runner, args=(runner_name,)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append('Race over!')
    return result



def scenario_3():
    global result
    result = []
    result.append('START RACE!!!!')
    threads = []
    for runner_name in runners:
        threads.append(Thread(target=runner,args=(runner_name,)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    result.append('Race over!')
    return result
