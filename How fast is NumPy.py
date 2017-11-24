
import numpy as np
from time import time

def how_long(func, *args):
    """Execute function with given arguments, and measure execution time."""
    t0 = time()
    result = func(*args) # all arguments are passed in as-is
    t1 = time()
    return result, t1 - t0

def manual_mean(arr):
    """compute mean (average) of all elements in the given 2D array."""
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range (0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size

def numpy_mean(arr):
    """Compute mean (average) using NumPy."""
    return arr.mean()


# START Just two excercises
def indexing_array_with_another_array():

    a = np.random.rand(5)

    #accessing using list of indices
    indices = np.array([1,1,2,3])
    print (a[indices])
    return a[indices]

def mask_array():

    a = np.array([(20, 25, 10, 23, 26, 32, 10,5,0),(0, 2, 50, 20, 0, 1, 28, 5, 0)])
    mean = a.mean()
    return a[a<mean]

    #accessing using list of indices
    indices = np.array([1,1,2,3])
    print (a[indices])
    return a[indices]
# END Just two excercises


def test_run():
    """Function called by test Run."""
    nd1 = np.random.random((1000, 10000)) # use a significantly large array

    # time the two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    #print ("Manual: {:.6f} ({^.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.))".format(res_numpy, res_manual))

    # Make sure both give us the same answer (upto some precision)
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    # Compute speedup
    speedup = t_manual / t_numpy
    print ("NumPy mean is", speedup, "times faster than manual for loops.")

if __name__ == "__main__":
    test_run()