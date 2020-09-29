"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q) The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
   is unusual in two ways: 
        (i) each of the three terms are prime, and, 
        (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
    What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from utils import timing_decorator, is_prime, get_digit_permutations
import numpy as np
from itertools import combinations

@timing_decorator
def prime_perms():
    selected = []
    for i in range(1000, 9999):
        if is_prime(i):
            allperms = sorted(list(set([k for k in get_digit_permutations(i) if len(str(k))==4 and is_prime(k)])))
            if len(allperms) >= 3:
                for ecomb in list(combinations(allperms,3)):
                    if set(np.diff(ecomb)) == set([3330]):
                        _s = "".join([str(k) for k in sorted(ecomb)])
                        if _s not in selected:
                            selected.append(_s)
    print('Concatenated Numbers : ', selected)

prime_perms()
