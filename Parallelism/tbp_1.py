import threading

result =[]
def my_func(thread_number):
    result.append(f'my_func called by thread N°{format(thread_number)}')


def scenario_1():
    threads = []
    global result
    result = []
    for i in range(10):
        threads.append(threading.Thread(target=my_func, args=(i,)))
        threads[-1].start()
        threads[-1].join()
    return result

def scenario_2():
    threads = []
    global result

    result = []

    for i in range(10):
        threads.append(threading.Thread(target=my_func, args=(i,)))
        threads[-1].start()
    for t in threads:
        t.join()

    return result



def scenario_3():
    threads = []
    global result
    result = []

    for i in range(10):
        threads.append(threading.Thread(target=my_func, args=(i,)))
        threads[-1].start()
        if i > 4:
            threads[-1].join()
            threads.pop(-1)
    for t in threads:
        t.join()
    return result


