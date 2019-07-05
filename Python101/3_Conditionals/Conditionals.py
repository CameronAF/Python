# 1. If statment
if 5 == 15 / 3:
  print("5 == 15 / 3")
if True:
  print("True")
if 5 != 5:
  print("5 != 5")
print()

# 2. Else statment
x = 3
if x > 3:
  print("Case 1")
if x <= 3:
  print("Case 2")
 
if x > 3:
  print("Case 1")
else:
  print("Case 2")
print()

# 3. Elif statement
def compare_to_five(y):
  if y > 5:
    return "Greater then"
  elif y < 5:
    return "Less then"
  else:
    return "Equals"
print(compare_to_five(10))
print()