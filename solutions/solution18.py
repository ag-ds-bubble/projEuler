"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)
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

num_pyramid = "3,\
7 4,\
2 4 6,\
8 5 9 3"

num_pyramid = "75,\
95 64,\
17 47 82,\
18 35 87 10,\
20 04 82 47 65,\
19 01 23 75 03 34,\
88 02 77 73 07 63 67,\
99 65 04 28 06 16 70 92,\
41 41 26 56 83 40 80 70 33,\
41 48 72 33 47 32 37 16 94 29,\
53 71 44 65 25 43 91 52 97 51 14,\
70 11 33 28 77 73 17 78 39 68 17 57,\
91 71 52 38 17 14 91 43 58 50 27 29 48,\
63 66 04 68 89 53 67 30 73 16 69 87 40 31,\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

num_pyr = prep_pyramid(num_pyramid)

print(sum_wordlenv2(num_pyr))
