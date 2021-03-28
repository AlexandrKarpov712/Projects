import time
import logging

def functionTime(func):
    def decorator(n):
        start_time = time.perf_counter()
        result = func(n)
        print(time.perf_counter() - start_time)
        return result
    return decorator

def loggingFunction(func):
    def decorator(n):
        logging.basicConfig(filename='log.log', level=logging.INFO)
        logging.info(func.__doc__)
        return func(n)
    return decorator

def countFunction(func):
    counters = {}
    def decorator(n):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(n)
    return decorator

@functionTime
@loggingFunction
@countFunction
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res