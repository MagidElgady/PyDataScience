# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at what pandas are and when they are used.

# What?
# Pandas are a software library written in Python and used to analyse and manipulate
# sets of tabular data.
# Pandas are built on top of Numpy and SciPy and so can be used with n-dimensional arrays
# and can be integrated with C++.

# Example


import pandas as pd

# Dictionary showing data about a website
XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], 'Visitors': [1000, 700, 6000, 1000, 400, 350],
           'Bounce_Rate': [20, 20, 23, 15, 10, 34]}

# Converts dictionary to dataframe
df = pd.DataFrame(XYZ_web)
print(df)
