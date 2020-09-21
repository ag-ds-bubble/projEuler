import time
import numpy as np

def timing_decorator(func):
    def wrapper(*arg, **kw):
        t1 = time.perf_counter_ns()
        res = func(*arg, **kw)
        t2 = time.perf_counter_ns()
        print(f'Total time taken : {np.round((t2-t1)/1e6, 3)} ms' )
        return res, func.__name__
    return wrapper


def eratosthenes_primegen():
    D={}
    p=2
    while True:
        if p not in D:
            yield p
            D[p*p] = [p]
        else:
            for q in D[p]:
                D.setdefault(p+q,[]).append(q)
            del D[p]
        p+=1


def check_palindrome(num):
    return str(num) == str(num)[::-1]