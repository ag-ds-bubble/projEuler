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
from utils import timing_decorator, check_palindrome
import numpy as np

@timing_decorator
def find_Lpal(N=3):
    maxN = 10**N-1
    minN = 10**(N-1)
    max_product = 0
    palin_list = []

    for i in reversed(range(minN,maxN+1)):
        for j in reversed(range(minN,maxN+1)):
            prod = i*j
            if prod<max_product:
                break
            if check_palindrome(prod) and prod > max_product:
                palin_list.append(prod)
                max_product = prod
                
    print(f'Largest palindrome : {max(palin_list)}')

find_Lpal(3)
