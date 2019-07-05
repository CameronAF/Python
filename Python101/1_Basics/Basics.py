# Ways to import
# 1) import math
# 2) from math import sqrt
# 3) from math import sqrt as s
# 4) import math as m
# 5) from math import *

# 1. assign and print
x,y = (5,2.75)
print('x:', x)
print('y:', y)
print()

# 2. numeric, bool, and casting
z = True
print(type(x))
print(type(y))
print(type(z))
print(int(y))
print(float(x))
print()

# 3. strings
print('George')
print("George")
txt =  "Dollars"
print(str(x) + " " + txt)
print("I'm " "fine") # plus not needed to concatincate
print('I\'m', 'fine') # comma is space
print()


# 4. line continuation (\)
print(4 * 5 + \
  2)
print()