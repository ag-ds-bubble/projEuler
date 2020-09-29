"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
        It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
from utils import timing_decorator
import numpy as np

@timing_decorator
def coin_sums(sumto=2):
    tot_ways = 0
    denoms = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2])
    denoms_maxc = np.uint8(1/(np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2])/sumto))
    print(denoms)
    print(denoms_maxc)
    print(np.prod(denoms_maxc))
    print()
    print(f'Number of different ways to sum to 2 : ', tot_ways)

coin_sums(1)
