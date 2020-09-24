"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
   
   For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
   A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
   abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
   the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known 
   that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
   
   Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from utils import timing_decorator, find_divisors
import numpy as np


@timing_decorator
def non_abundantsums(N=28123):
    abundant_nos = []
    for i in range(1,N):
        divisor_sum1 = sum([k for k in list(find_divisors(i)) if k!= i])
        if divisor_sum1 > i:
            abundant_nos.append(i)

    abundant_pairsums = []
    for i in abundant_nos:
        for j in abundant_nos:
            if i!=j:
                _sum = i+j
                if _sum<N:
                    abundant_pairsums.append(_sum)

    _non_abundantsums = int(0.5*(N)*(N+1)) - sum(list(set(abundant_pairsums)))
    print(f'Sum of the all Non-abundant sums below {N} = ', _non_abundantsums)

non_abundantsums()
