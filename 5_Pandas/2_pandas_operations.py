# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at all the basic operations that can be performed using pandas.

import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt

# Dictionary showing data about a website
XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], 'Visitors': [1000, 700, 6000, 1000, 400, 350],
           'Bounce_Rate': [20, 20, 23, 15, 10, 34]}

# Converts dictionary to dataframe
df = pd.DataFrame(XYZ_web)


# Slicing

# Only gets the first rows from the top
print("Gets the first 2 rows:\n", df.head(2))

# Only gets the last rows from the bottom
print("Gets the last 2 rows:\n", df.tail(2))


# Merging: Merges sets of data based on what they have in common

df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

print("Before dataframes were merged:\n", df1)
print("Before dataframes were merged:\n", df2)

# Merges the 2 dataframes but keeps the HPI column in common
# i.e. only HPI shows up without x or y
merge = pd.merge(df1, df2, on="HPI")

print("After the data was merged:\n", merge)

# Joining: Joins sets of data based on index value (must have same columns and rows
# or there will be a mismatch)

df3 = pd.DataFrame({"Int Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

df4 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [
                   1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])

# NaN shows up as we're missing data for 2002 in df4
joined = df3.join(df4)
print(joined)

# Changing index and column headers

df = pd.DataFrame({'Day': [1, 2, 3, 4, 5, 6], 'Visitors': [1000, 700, 6000, 1000, 400, 350],
                   'Bounce_Rate': [20, 20, 23, 15, 10, 34]})

# Names index value as Day
df.set_index("Day", inplace=True)
# Shows graph in 538 style
style.use("fivethirtyeight")

# Renames visitors to users
df = df.rename(columns={"Visitors": "Users"})

# df.plot()
# plt.show()

# Concatenate: Adds a new row or column to existing dataset

df5 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

df6 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int Rate": [2, 1, 2, 3], "IND_GDP": [
                   50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

Concat = pd.concat([df5, df6])

print(Concat)

# Data munging: Converts file from one format to another

supermarkets = pd.read_csv("5_Pandas\\supermarkets.csv")

supermarkets.set_index("ID", inplace=True)

# Displays the dataframe
print(supermarkets)

# Converts file to HTML
supermarkets.to_html("5_Pandas\\super.html")
