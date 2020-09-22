"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

from utils import timing_decorator
import numpy as np

@timing_decorator
def pythagorean_triplet(N=1000):
    a,b,c = 0,0,0
    for i in range(1,50):
        a = i
        b = (5e5-1000*a)/(1000-a)
        c = 1000-a-b
        # if b-int(b)==0:
        print(a,b,c)

pythagorean_triplet()
