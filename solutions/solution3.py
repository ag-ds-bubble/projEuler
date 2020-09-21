"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""
from utils import timing_decorator

@timing_decorator
def find_fiboeven():
    thresh = 4_000_000
    nums = [1,2]
    total = 2
    while nums[-1]<thresh:
        next_inseq = nums[-1]+nums[-2]
        nums.append(next_inseq)
        if next_inseq%2==0:
            total += next_inseq

    print('Last calculated number in Fibonacci Sequence : ', nums[-1])
    print('Total : ', total)


find_fiboeven()
