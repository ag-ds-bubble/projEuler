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

def find_factors(num):
    curr_num = num
    factors = [1]
    i = 2
    if num==1:
        return factors
    while curr_num>1:
        # print(curr_num, i)
        if curr_num%i==0:
            curr_num = curr_num/i
            factors.append(i)
            i = 2
        else:
            i+=1

    return factors

