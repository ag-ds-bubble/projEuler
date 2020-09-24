"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) n! means n × (n − 1) × ... × 3 × 2 × 1
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    Find the sum of the digits in the number 100!
"""
from utils import timing_decorator, get_factorial
import numpy as np

@timing_decorator
def sum_fact(N=10):
    totalsum = sum(int(k) for k in str(get_factorial(N)))
    print(f'Sum of the all digits in {N}! = ', totalsum)


sum_fact(100)