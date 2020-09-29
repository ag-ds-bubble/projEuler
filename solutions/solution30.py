"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

                1634 = 14 + 64 + 34 + 44
                8208 = 84 + 24 + 04 + 84
                9474 = 94 + 44 + 74 + 44
                As 1 = 14 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from utils import timing_decorator
import numpy as np

@timing_decorator
def digit_n_power(power=5):
    # Figure out the upper limit
    llimit,ulimit=0,int(1e9)
    for i in range(1,100):
        maxpossible = i*(9**power)
        if i>=len(str(maxpossible)):
            ulimit = int("".join(['9']*i))
            print(llimit, ulimit)
            break
    nums = []
    for i in range(llimit, ulimit):
        if sum([int(k)**power for k in list(str(i))]) == i and i not in [0,1]:
            nums.append(i)

    print(f'Sum : ', sum(nums))

digit_n_power()

