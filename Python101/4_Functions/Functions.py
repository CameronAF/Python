# 1. Functions without Parameter
def simple():
  print("Printing from my first Function")
simple()
print()

# 2. Function with Paramater
def plus_ten(a):
  return a + 10
print('plus_ten(2):', plus_ten(2))
print('plus_ten(10):', plus_ten(10))
print()

# 3. Functions within functions
def wage(w_hours):
  return w_hours * 25

def with_bonus(w_hours):
  return wage(w_hours) + 50

print('wage(8), with_bonus(8)', wage(8), with_bonus(8))
print()

# 4. Function with Multiple Params
def subtract_bc(a,b,c):
  result = a - b * c
  print("Param a =", a)
  print("Param b =", b)
  print("Param c =", c)
  return result

print('subtract_bc():', subtract_bc(10,3,2))
print('subtract_bc():', subtract_bc(b=3,a=10,c=2))
print()

# 5. Some build in Functions
type(10)
int(5.0)
float(3)
str(500)
max(10,20,30)
min(10,20,30)
abs(-20)
lst = [1,2,3,4]
sum(lst)
round(3.5555,2)
round(3.5)
2 ** 10
pow(2,10)
len('Mathematics')