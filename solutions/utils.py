import time
import numpy as np

def timing_decorator(func):
    def wrapper(*arg, **kw):
        t1 = time.perf_counter_ns()
        res = func(*arg, **kw)
        t2 = time.perf_counter_ns()
        print(f'Total time taken : {np.round((t2-t1)/1e9, 3)} secs' )
        return res, func.__name__
    return wrapper