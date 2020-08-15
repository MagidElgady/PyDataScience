# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at the integration functions that can be used within the
# scipy library.

# Scipy has to be imported first before getting
# all of the functions!
import scipy
from scipy import integrate, special

# General Integration - quad function
# Used for finding integral of a function with 1 variable

# Integrates 10 to the power of x with limits between 0 and 1
# Note: Use the lambda function to add the function you
# want to integrate.
i = scipy.integrate.quad(lambda x: special.exp10(x), 0, 1)
# Outputs the area of the enclosed space for the above function
print("Integral of 10^x between 0 and 1 is:", i)


# Double Integration - dblquad function
# Used for finding integral of a function with 2 variables


# Defines the function x*y^2
def e(x, y): return x * y ** 2


# Sets x to positive
def f(x): return 1


# Sets y to negative
def g(x): return -1


# Performs the integration with limits between 0 and 2
h = integrate.dblquad(e, 0, 2, f, g)
print("Integral of x*-y^2 is:", h)
