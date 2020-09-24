"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by 
    its alphabetical position in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 
    938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    What is the total of all the name scores in the file?
"""
from utils import timing_decorator, find_divisors
import numpy as np
import re


@timing_decorator
def calc_namescore(fnames):
    total_score = 0
    fnames = sorted(fnames)
    for nidx, name in enumerate(fnames):
        namescore = sum([int(ord(c)&31) for c in name])
        poscore = nidx+1
        total_score += poscore*namescore
    print(f'Total names score = ', total_score)

fnames = list(open('raw_data/p022_names.txt', 'r'))[0]
fnames = [re.sub('"','',k) for k in fnames.split(',')]
calc_namescore(fnames)
