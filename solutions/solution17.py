"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
    and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from utils import timing_decorator
import numpy as np
from num2words import num2words
import re

@timing_decorator
def sum_wordlen(N=1000):
    total_len=0
    for i in range(1,N+1):
        txt = num2words(i)
        txt = re.sub(' ', '', txt)
        txt = re.sub('-', '', txt)
        total_len+=len(txt)

    print(f'Sum of all the words in cummulative words : {total_len}')

sum_wordlen()
