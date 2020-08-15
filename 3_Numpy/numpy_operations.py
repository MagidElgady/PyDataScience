# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at the basics of operations you can do
# with numpy e.g. find the dimension of array, size of each element,
# size of array etc.

import numpy as np

# 2D array
a = np.array([(1, 2, 3), (4, 5, 6)])

# Use ndim to get the dimensions of an array
print("Dimensions of a:", a.ndim)

# Use itemsize to get the byte size of each element
print("Byte size of each element in a:", a.itemsize, "bytes")

# Use dtype to get the type of element in the array
print("Data type of each element in a:", a.dtype)

# Use size to get number of elements in the array
print("Number of elements in a:", a.size)

# Use shape to get number of rows and columns (rows, columns)
print("Number of rows and columns:", a.shape)

# You can reshape the array into a different shape
# as long as it matches the number of elements
# Following creates 1 row with 6 columns
b = a.reshape(1, 6)

print("Array a before reshape:\n", a)
print("Array a after reshape:", b)

# Indexing is where we get the specific
# element (index) from an array
print(
    "This gets the 3rd element (index 2) from the 1st row (index 0):", a[0, 2])

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

# Slicing is where we get a portion of the numpy array
print(
    "This gets the 3rd element (index 2) from the 1st and 2nd (Index 0 and Index 1) row", a[0:2, 2])

# Linspace gets values between 2 points equal spaced out
# The following gets values from 0 to 3 and obtains
# 5 elements total
a = np.linspace(0, 3, 5)

print("This gets 5 numbers between 0 and 3:", a)

a = np.array([1, 2, 3])

# Gets maximum value from array
print("Maximum value in array a is:", a.max())

# Gets minimum value from array
print("Minimum value of array:", a.min())

# Gets sum from array
print("Sum of array:", a.sum())

a = np.array([(1, 2, 3), (4, 5, 6)])

# Axis 0 refers to columns
print("Sum of columns:", a.sum(axis=0))
# Axis 1 refers to rows
print("Sum of rows:", a.sum(axis=1))

# Gets the square root of each element
# in the array
print("Square root of each element:\n", np.sqrt(a))

# Gets the standard deviation (average
# deviation from the mean)
print("Standard deviation of array:", np.std(a))

a = np.array([(1, 2, 3), (4, 5, 6)])

b = np.array([(1, 2, 3), (4, 5, 6)])

# Adding numpy arrays (like a matrix) is just simple
# a+b addition
print("When you add each element in each array:\n", a+b)

# Subtracting numpy arrays is the same as addition
print("When you subtract each element in each array:\n", a - b)

# Multiplication and division work the same way (like in matrices)
print("When you multiply each element in each array:\n", a * b)
print("When you divide each element in each array:\n", a/b)

# Vertical stacking is where we put arrays on top of
# each other
print("Vertical stacking of arrays a and b:\n", np.vstack((a, b)))

# Horizontal stacking is where we put arrays side by side
print("Horizontal stacking of arrays a and b:\n", np.hstack((a, b)))

# Use the ravel method to convert an array to a single column
print("Converts array a to single column:", np.ravel(a))
