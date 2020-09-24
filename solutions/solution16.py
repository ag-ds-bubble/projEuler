"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
"""
from utils import timing_decorator, SUPERSCRIPT_MAP
import numpy as np

@timing_decorator
def sum_2pow(N=1000):
    ptxt = "".join([SUPERSCRIPT_MAP[k] for k in list(str(N))])
    sum_ofdigits = sum([int(k) for k in list(str(2**N))])
    print(f'Sum of all the digits in the 2{ptxt} : {sum_ofdigits}')

sum_2pow()
