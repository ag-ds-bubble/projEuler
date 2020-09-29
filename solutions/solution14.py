"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  The following iterative sequence is defined for the set of positive integers:
                n → n/2 (n is even)
                n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from utils import timing_decorator, find_factors
import numpy as np

chain_mapping={}

def get_chainlen(num):
    global chain_mapping
    chain_len=0
    chain=[num]
    while num!=1:
        if num in chain_mapping:
            return len(chain)+chain_mapping[num]-1
        if num%2==0:
            num=int(num/2)
        else:
            num=int(3*num+1)
        chain.append(num)
    chain_len = len(chain)
    for i in range(len(chain)):
        if i not in chain_mapping:
            chain_mapping[chain[i]] = len(chain[i:])
    return chain_len

@timing_decorator
def logest_collatz(N=1e6):
    num = 0
    cno = 0
    clen = 0
    
    for i in range(1,int(N)):
        curr_clen = get_chainlen(i)
        if curr_clen>clen:
            cno = i
            clen=curr_clen
    print(f'Starting number with longest collatz chain under < {N} is {cno}, with chain length of {clen}')

logest_collatz()