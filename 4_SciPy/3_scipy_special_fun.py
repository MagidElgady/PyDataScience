# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at some of the special mathematical functions in SciPy such as
# exponential and trigonometric functions.

# We need to import special the function
# from the scipy library
from scipy import special

# Exponential Functions

# Calculates 10 to the power of 2
a = special.exp10(2)
# Outputs 10 squared
print("10 squared =", a)

b = special.exp2(3)
print("2 cubed =", b)


# Trigonometric Functions

# Gets the sine value of an angle in degrees
c = special.sindg(90)
print("The sine value of 90 degrees is:", c)

# Gets the cosine value of of an angle in degrees
d = special.cosdg(0)
print("The cosine value of 0 degrees is:", d)
