"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
"""

from utils import timing_decorator, eratosthenes_primegen
import numpy as np

@timing_decorator
def nth_prime(N=10001):
    prime_gen = eratosthenes_primegen()
    for _ in range(N):
        prime_no=next(prime_gen)
    print(f'{N}th prime number : {prime_no}')

nth_prime()
