import multiprocessing


def function_square(data):
    return data * data


def function_pow_3(data):
    return data * data * data


inputs = list(range(0, 100))


def scenario_1():
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    return 'Pool :', pool_outputs


def scenario_2():
    with multiprocessing.Pool(processes=4) as pool:
        pool_outputs = pool.map(function_square, inputs)
    return pool_outputs


def scenario_3():
    with multiprocessing.Pool(processes=4) as pool:
        pool_outputs = pool.map(function_pow_3, inputs)
    return pool_outputs



