import random
import threading
import time
result =[]


def function_a(i):
    result.append(str(threading.current_thread().name )+ '----> starting \n')
    time.sleep(i)
    result.append(str(threading.current_thread().name) + '----  exiting \n')


def function_b(i):
    result.append(str(threading.current_thread().name )+ '----> starting \n')
    time.sleep(i)
    result.append(str(threading.current_thread().name) + '----> exiting \n')


def function_c(i):
    result.append(str(threading.current_thread().name )+ '----> starting \n')
    time.sleep(i)
    result.append(str(threading.current_thread().name) + '----> exiting \n')


def scenario_1():

    global result
    result = []
    thread_names = ['function_A', 'function_B', 'function_C']
    threads = []
    threads.append(threading.Thread(name=thread_names[0], target=function_a, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[1], target=function_b, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[2], target=function_c, args=(random.randint(0, 10),)))
    for thread in threads:
        thread.join()
    return result


def scenario_2():

    global result
    result = []
    thread_names = ['function_A', 'function_B', 'function_C']
    threads = []
    threads.append(threading.Thread(name=thread_names[0], target=function_a, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[1], target=function_b, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[2], target=function_c, args=(random.randint(0, 10),)))
    for thread in threads:
        thread.start()
        thread.join()
    return result

def scenario_3():

    global result
    result = []
    thread_names = ['function_A', 'function_B', 'function_C']
    threads = []
    threads.append(threading.Thread(name=thread_names[0], target=function_a, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[1], target=function_b, args=(random.randint(0, 10),)))
    threads.append(threading.Thread(name=thread_names[2], target=function_c, args=(random.randint(0, 10),)))
    threads[1].start()
    threads[2].start()
    threads[2].join()
    threads[1].join()
    threads[0].start()
    threads[0].join()
    return result

