"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

                                        21 22 23 24 25
                                        20  7  8  9 10
                                        19  6  1  2 11
                                        18  5  4  3 12
                                        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
from utils import timing_decorator
import numpy as np

@timing_decorator
def diag_sum(N=1001):
    nums = [1]
    for i in range(3,N+1,2):
        for _ in range(4):
            nums.append(nums[-1]+i-1)
    print(f'Sum of the spiral matrix of {N}x{N} : ', sum(nums))

diag_sum()

