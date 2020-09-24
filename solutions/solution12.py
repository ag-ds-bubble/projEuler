"""
Author : Achintya Gupta
Date Created : 24-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    Let us list the factors of the first seven triangle numbers:
            1: 1
            3: 1,3
            6: 1,2,3,6
            10: 1,2,5,10
            15: 1,3,5,15
            21: 1,3,7,21
            28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.
    What is the value of the first triangle number to have over five hundred divisors?
"""

from utils import timing_decorator, find_divisors
import numpy as np

@timing_decorator
def tiangle_divisor_count(N=500):
    num=0
    factors=[]
    while True:
        num+=1
        traingle_num = int(0.5*num*(num+1))
        factors = list(find_divisors(traingle_num))
        if len(factors)>N:
            break
    
    print(f'First triangle number with over {N} divisors: {traingle_num}, with {len(factors)} factors')

tiangle_divisor_count(500)
