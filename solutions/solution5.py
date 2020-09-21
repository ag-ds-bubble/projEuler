"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from utils import timing_decorator, find_factors
import numpy as np


@timing_decorator
def find_min_prod(N=20):
    D = {}
    for i in range(1, N+1):
        _factors = find_factors(i)
        fact, cnts = np.unique(_factors, return_counts=True)
        for fact, cnts in zip(fact, cnts):
            if fact in D:
                D[fact] = max(cnts, D[fact])
            else:
                D[fact] = cnts
    num = np.prod([k**v for k,v in D.items()])
    print(f'Minimum number divisible by all numbers between 1 <-> {N} : {num}')

find_min_prod(20)
