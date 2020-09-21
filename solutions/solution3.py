"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
"""
from utils import timing_decorator, eratosthenes_primegen
import numpy as np

@timing_decorator
def find_Lprime(num=600851475143):
    prime_gen = eratosthenes_primegen()
    currnum = num
    all_primes = []
    while currnum > 1:
        next_prime = next(prime_gen)
        if currnum % next_prime == 0:
            all_primes.append(next_prime)
            currnum/=next_prime
            print(f'Found a prime factor -> {next_prime} , Current Number {currnum}')

find_Lprime()
