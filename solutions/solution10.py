"""
Author : Achintya Gupta
Date Created : 24-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""

from utils import timing_decorator, eratosthenes_primegen
import numpy as np

@timing_decorator
def primesum_below(N=2e6):
    next_primegen = eratosthenes_primegen()
    next_prime = next(next_primegen)
    total_sum = 0
    while next_prime<N:
        total_sum+=next_prime
        next_prime = next(next_primegen)
    print(f'Sum of all primes below {N} : {total_sum}')

primesum_below()
