# 1. For Loop
even = [0,2,4,6,8,10,12,14,16,18,20]
print('For loop a List:')
for n in even:
  # single line print all
  print(n, end=" ")
print('\n')

# 2 While Loops
x = 0 
print('While loop:')
while x <= 20:
  # single line print all
  print(x, end=" ")
  x += 2
print('\n')

# 3 range
print('Using range(start, stop, step)')
lst = list(range(10))
print('Range(10):', lst)
lst = list(range(3,7))
print('Range(3,7):', lst)
lst = list(range(1,20,2))
print('Range(1,20,2):', lst)
print('Looping range():', end=" ")
for n in range(20):
  if x % 2 == 0:
    print(n, end=" ")
  else:
    print('Odd', end=" ")
print()
print('Looping range(List):', end=" ")
for i in range(len(even)):
  print(even[i], end=" ")
print('\n')

# 4 looping through dictionary
prices = {'beef' : 4, 'cheese' : 5, 'buns' : 2 }
quantity = {'beef' : 6, 'cheese' : 10, 'buns' : 0 }
money_spent = 0
for i in prices:
  money_spent = money_spent + (prices[i]*quantity[i])
print('Total spent:', money_spent)