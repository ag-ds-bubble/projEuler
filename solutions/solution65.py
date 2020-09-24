"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

                                                    3
                                                    7 4
                                                    2 4 6
                                                    8 5 9 3
    That is, 3 + 7 + 4 + 9 = 23.
    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! 
    If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
from utils import timing_decorator
import numpy as np
import re

def prep_pyramid(pyr):
    nums = [[e for e in k.split()] for k in pyr.split(',')]
    cols = 2*max([len(k) for k in nums])-1
    rows = len(nums)
    pyramid = np.zeros((rows, cols), np.uint32)
    nidx = 0
    for eidx, ep in enumerate(reversed(nums)):
        nidx = eidx
        # Add intermediaries
        for e_elem in ep:
            pyramid[rows-eidx-1,nidx] = e_elem
            nidx +=2
    return pyramid

def sum_wordlenv2(num_pyr):
    rows, cols = num_pyr.shape
    if rows == 2:
        # Return the Maximum Sum
        for eelem in np.nonzero(num_pyr[-2,:])[0]:
            num_pyr[-2,eelem] = max(num_pyr[-2,:][eelem]+num_pyr[-1,:][eelem-1], num_pyr[-2,:][eelem]+num_pyr[-1,:][eelem+1])
        return np.max(num_pyr[0,:])
    else:
        for eelem in np.nonzero(num_pyr[-2,:])[0]:
            num_pyr[-2,eelem] = max(num_pyr[-2,:][eelem]+num_pyr[-1,:][eelem-1], num_pyr[-2,:][eelem]+num_pyr[-1,:][eelem+1])
        num_pyr = num_pyr[:-1,:]
        return sum_wordlenv2(num_pyr)

num_pyramid  = "".join([re.sub('\n', ',', k) for k in list(open('raw_data/p067_triangle.txt', 'r'))])[:-1]
num_pyr = prep_pyramid(num_pyramid)

print(sum_wordlenv2(num_pyr))
