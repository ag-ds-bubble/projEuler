import time
import numpy as np
from math import factorial
import itertools

SUPERSCRIPT_MAP = {'1' : '¹',
                   '2' : '²',
                   '3' : '³',
                   '4' : '⁴',
                   '5' : '⁵',
                   '6' : '⁶',
                   '7' : '⁷',
                   '8' : '⁸',
                   '9' : '⁹',
                   '0' : '⁰'}

def timing_decorator(func):
    def wrapper(*arg, **kw):
        t1 = time.perf_counter_ns()
        res = func(*arg, **kw)
        t2 = time.perf_counter_ns()
        ttaken = str(np.round((t2-t1)/1e6, 3)).zfill(10)
        print(f'Total time taken : {ttaken} ms' )
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

def find_divisors(num):
    large_divisors = []
    for i in range(1, int(np.sqrt(num) + 1)):
        if num % i == 0:
            yield i
            if i*i != num:
                large_divisors.append(int(num / i))
    for divisor in reversed(large_divisors):
        yield divisor

def get_factorial(num):
    return factorial(num)

def fibbonaci_gen():
    fibbonaci_list = [0,1]
    while True:
        yield fibbonaci_list[-1]
        fibbonaci_list.append(fibbonaci_list[-1]+fibbonaci_list[-2])

def is_prime(num):
    for i in range(2,int(num**0.5)):
        if num%i==0:
            return False
    return True

def get_digit_permutations(num):
    temp = list(itertools.permutations([int(k) for k in list(str(num))]))
    all_perms = [int("".join([str(j) for j in k])) for k in temp]
    return all_perms


