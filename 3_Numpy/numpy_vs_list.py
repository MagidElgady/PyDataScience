# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# Numpy is much faster way of way representing data compared with lists,
# They take up less space in memory and are much more convenient.
# We'll compare the execution times of a numpy array and a list.

import numpy as np

import time

import sys

# List of numbers between 0 - 999
S = range(1000)

# Gets size of 1 element in list and multiply by length
# of list to get size of list
print("Space taken by list:", sys.getsizeof(5) * len(S))

# Creates numpy array between 0 - 999
D = np.arange(1000)

# Gets size of numpy array (much easier than list)
print("Space taken by nimpy:", D.size*D.itemsize)

# Execution time

SIZE = 1000000

# Stores all numbers between 0 - SIZE
# in list
L1 = range(SIZE)
L2 = range(SIZE)

# Stores all numbers between 0 - SIZE
# in numpy array
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

# Starts runtime stopwatch
start = time.time()

# Adds each number in each list and stores in
# result list (requires list comp to do this)
result = [(x, y) for x, y in zip(L1, L2)]

# Outputs runtime to finish
print("Time taken for list:", (time.time() - start)*1000, "ms")

# Starts runtime stopwatch
start = time.time()

# Adds each number in each array; much easier than lists
result = A1 + A2

# Outputs runtime to finish
print("Time taken for numpy:", (time.time() - start)*1000, "ms")
