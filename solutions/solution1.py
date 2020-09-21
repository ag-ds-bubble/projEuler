"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
from utils import timing_decorator

@timing_decorator
def find_35sum():
    total = []
    for i in range(1000):
        if (i%3==0) or (i%5==0):
            total.append(i)
    total = list(set(total))
    print('Solution : ', sum(total))

find_35sum()
