# 1. List [value, ... ]
  # add and remove
Participants = ['John', 'Leila', 'Gregory','Cate']
print('List:', Participants)
print('List at 1:', Participants[1])
print('List at -1:', Participants[-1])
print('List \'Gregory\' at index:', Participants.index('Gregory'))
Participants[3] = 'Maria'
print('List set at 3:', Participants)
del Participants[2]
print('List del at 2:', Participants)
Participants.append('Dwayne')
print('List append:', Participants)
Participants.extend(['George','Catherine'])
print('List extend:', Participants)
  # length
print('length of first element:', len(Participants[0]))
print('length of the list:', len(Participants))
  # slice
print('List slice [1:3]:', Participants[1:3])
print('List slice [:2]:', Participants[:2])
print('List slice [4:]:', Participants[4:])
print('List slice [-2:]:', Participants[-2:])
  # order
Participants.sort()
print('List sorted:', Participants)
Participants.sort(reverse=True)
print('List reverse sorted:', Participants)
  # list of list
Newcomers = ['Joshua','Brittany']
Participants = [Participants, Newcomers]
print('List + List2:', Participants)
print()

# 2. Tuples (value, ...)
x = (40, 41, 42)
y = 50,51,52
a,c,b = 1,4,5 #tupal assignment
List = [x,y]
print('Tuple x:', x[0])
print('Tuple x at index 1:', x[0])
print('List of Tuples:', List)
 # Split into Tuple
(age, years) = '30,17'.split(',')
print('Tuple with Age:', age)
print('Tuple with Years:', years)
 # Tuplul as function return
def square_info(x):
  A = x ** 2
  P = 4 * x
  return A,P
print('Area and Perimeter', square_info(3))
print()

# 3. Dictionaries {key : value, ...} - Keys and Key-value pairs
dict = {'k1':'cat', 'k2':'dog', 'k3':'mouse', 'k4':'fish'}
print('Dictionary:', dict)
print('Dictionary k2:', dict['k2'])
dict['k5'] = 'parrot'
print('Dictionary add:', dict)
dict['k2'] = 'squirrel'
print('Dictionary replace:', dict)
print('Dictionary get k3', dict.get('k3'))
print('Dictionary get k6', dict.get('k6'))
dict = {}
print('Empty Dictionary:', dict)