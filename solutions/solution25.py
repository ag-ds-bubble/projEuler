"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) The Fibonacci sequence is defined by the recurrence relation:
        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
        Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144
        The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from utils import timing_decorator, fibbonaci_gen
import numpy as np

@timing_decorator
def digit1_1000fib():
    num=''
    idx = 0
    fgen = fibbonaci_gen()
    while True:
        num = str(next(fgen))
        idx+=1
        if len(num)==1000:
            break
    print(f'Index of first term with 1000 digits : ', idx, '; Number : ',  num)

digit1_1000fib()

