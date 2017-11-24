"""


Numpy is lib that is wrapper around C code. It focuses on matrices which are called in the arrays.
While Pandas is a kind of wrapper for NumPy

dataframe is a wrapper around ndarray - access columns by symbols and rows by dates
ndarray - is data from df

* dataframes can be joined
* rows with NA values can be dropped from the DF

nd1 = df1.values

Outline:

Create a NumPy array:
    from a pandas dataframe: pandas.DataFrame.values
    from a Python sequence: numpy.array
    with constant initial values: numpy.ones, numpy.zeros
    with random values: numpy.random
Access array attributes: shape, ndim, size, dtype
Compute statistics: sum, min, max, mean
Carry out arithmetic operations: add, subtract, multiply, divide
Measure execution time: time.time, profile
Manipulate array elements: Using simple indices and slices, integer arrays, boolean arrays




"""

"""Locate maximum value."""

import numpy as np
import time

def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here
    max_val = a.argmax()
    return max_val


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print ("Array:", a)

    # Find the maximum and its index in array
    print ("Maximum value:", a.max())
    print ("Index of max.:", get_max_index(a))

    t1 = time.time()
    print ("ML4T")
    t2 = time.time()
    print ("The time taken by print statement is ", t2 - t1, " seconds")


if __name__ == "__main__":
    test_run()
