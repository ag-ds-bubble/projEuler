"""
Author : Achintya Gupta
Date Created : 22-09-2020
"""

"""
Problem Statement
------------------------------------------------
Q)  Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
"""
from utils import timing_decorator, get_factorial
import numpy as np

@timing_decorator
def num_routes(N=20):
    no_paths = get_factorial(N*2)/get_factorial(N)/get_factorial(N)
    print(f'Number of possible paths in {N}x{N} grid : {int(no_paths)}')

num_routes()
