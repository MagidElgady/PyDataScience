# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lessons looks at generator expressions and how they can be
# used to create iterators.


f = range(6)

print("List comp", end=":")
# Example of list comprehension
q = [x + 2 for x in f]
# All values are printed at once
print(q)

print("gen exp", end=":")
# Generator expression as a tuple
r = (x+2 for x in f)

print(r)
# Outputs all the values in x
# 1 by 1
for x in r:
    print(x)
