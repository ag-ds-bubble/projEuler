"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
                 the proper divisors of 284 are 1, 2, 4, 71 and 142 ______________________________ so d(284) = 220.
    Evaluate the sum of all the amicable numbers under 10000.
"""
from utils import timing_decorator, find_divisors
import numpy as np


@timing_decorator
def sum_amicablepair(N=10000):
    amicable_nos = []
    for i in range(N):
        divisor_sum1 = sum([k for k in list(find_divisors(i)) if k!= i])
        divisor_sum2 = sum([k for k in list(find_divisors(divisor_sum1)) if k!= divisor_sum1])
        if i == divisor_sum2 and divisor_sum1 != divisor_sum2:
            print(i, divisor_sum1, divisor_sum2)
            amicable_nos.append(i)
    print(f'Sum of the all Amicable Pair below {N} = ', sum(amicable_nos))


sum_amicablepair()
