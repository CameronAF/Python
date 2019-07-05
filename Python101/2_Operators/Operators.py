# 1. Simple Operators and Operands
print('addition 1 + 2:', 1 + 2)
print('subtraction 3 - 5:', 3 - 5)
print('division 15 / 3:', 15 / 3)
print('division 16 / 3:', 16 / 3)
print('remainder 16 % 3:', 16 % 3)
print('multiplication 5 * 3:', 5 * 3) 
x =  5 ** 3
print('power 5 ** 3:', x)
print()

# 2. Comparison operators
print('x equals 125:', x == 125)
print('x equals 126:', x == 126)
print('10 not equal 10:', 10 != 10)
print('10 not equal 15:', 10 != 15)
print('100 greater then 50:', 100 > 50)
print('100 less then 50:', 100 < 50)
print('15 greater then or equal 20:', 15 >= 10 + 10)
print('15 less then or equal 15:', 15 <= 10 + 5)
print()

# 3. logical operators 
# order of execution: not > and > or
print('True and True:', True and True)
print('True and False:', True and False)
print('True or False:', True or False)
print('False or False:', False or False)
print('not True:', not True)
print('3 > 5 and 10 <= 20:', 3 > 5 and 10 <= 20)
print('True and not True:', True and not True)
print('False or not True and True:', False or not True and True)
print('False and not True or True:', False and not True or True)
print()

# 4. Identity Operators
print('5 is 6:', 5 is 6)
print('5 == 6:', 5 == 6)
print('5 is not 6:', 5 is not 6)
print('5 != 6:', 5 != 6)
print()

# 5. indexing (get 4th letter)
print("get 4th letter in Friday is", "Friday"[3])
print()