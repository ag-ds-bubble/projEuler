"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
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
