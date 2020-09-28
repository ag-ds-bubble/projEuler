"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
   If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
   The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210
   What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from utils import timing_decorator, get_factorial
import numpy as np

def recurr_loop(nums, nth, selected_nums = [], totald = 10):
    nums = sorted([k for k in nums if k not in selected_nums])
    total_digits = len(nums)
    blank_spaces = total_digits-1
    blank_combin = get_factorial(blank_spaces)
    if len(selected_nums) == totald-1:
        selected_nums = [str(k) for k in selected_nums+nums]
        return int("".join(selected_nums))
    numidx = int(np.floor(nth/blank_combin)) if nth%blank_combin != 0 else int(np.floor(nth/blank_combin))-1
    selected_digit = nums[numidx]
    selected_nums.append(selected_digit)
    return recurr_loop(nums, nth-blank_combin*numidx, selected_nums)

@timing_decorator
def nth_lexiperm(num_list=[0,1,2,4,3,5,6,7,8,9],N=1_000_000):
    perm_comb = recurr_loop(nums=num_list, nth=N)
    print(f'{N}`th Lexicographic permutation : ', perm_comb)

nth_lexiperm()

