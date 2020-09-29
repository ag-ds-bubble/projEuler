"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
   Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
from utils import timing_decorator
import numpy as np

@timing_decorator
def self_power(lastn=10):
    temp = 0
    for i in range(1,1000):
        temp+=i**i
    print(str(temp)[-10:])

self_power()
