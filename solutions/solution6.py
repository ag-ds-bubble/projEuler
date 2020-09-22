"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The sum of the squares of the first ten natural numbers is, 385
    The square of the sum of the first ten natural numbers is, 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 2640
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from utils import timing_decorator, find_factors
import numpy as np


@timing_decorator
def find_min_prod(N=100):
    prod = ((N)*(N+1))/2
    prod *= (3*(N**2) - N -2)/6
    print(f'Difference between the sum of the squares of the first {N} natural numbers and the square of the sum: {prod}')

find_min_prod()
