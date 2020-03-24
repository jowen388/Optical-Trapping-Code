#!/usr/bin/env python


import numpy as np
from datetime import datetime

def moving_average(a, n) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

a = np.arange(20)
print(a)
print(moving_average(a, 10))
