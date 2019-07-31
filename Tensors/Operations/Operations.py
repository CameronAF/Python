import numpy as np

# Create Matricies
m1 = np.array([[5,12,6],[-3,0,14]])
print('m1 is the matric \n', m1, '\n')
m2 = np.array([[9,8,7],[1,3,-5]])
print('m2 is the matric \n', m2, '\n')

# Addition
print('m1 + m2 = \n', m1 + m2, '\n')

# Subtraction
print('m1 - m2 = \n', m1 - m2, '\n')

# Create Vectors
v1 = np.array([1,2,3,4,5])
print('v1 is the vector \n', v1, '\n')
v2 = np.array([5,4,3,2,1])
print('v2 is the vector \n', v2, '\n')

# Addition
print('v1 + v2 = \n', v1 + v2, '\n')

# Subtraction
print('v1 - v2 = \n', v1 - v2, '\n')

# Addition and Subtraction with scalers
print('m1 + 2 = \n', m1 + 2, '\n')
print('m1 - 1 = \n', m1 - 1, '\n')
print('v1 + 3 = \n', v1 + 3, '\n')
print('v1 - 2  = \n', v1 - 2, '\n')

# Transposing
print('m1 is the matric \n', m1, '\n')
print('m1^T is the matric \n', m1.T, '\n')
print('v1 is the vector \n', v1, '\n')
print('v1^T is the vector \n', v1.T, '\n')
print('v1 reshaped then Transposed is \n', v1.reshape(1,5).T, '\n')

# Multiplication/Dot Product
v1 = np.array([2,8,-4])
print('v1 is the vector \n', v1, '\n')
v2 = np.array([1,-7,3])
print('v2 is the vector \n', v2, '\n')

print('v1 x v2  = \n', np.dot(v1,v2), '\n')
print('v1 x 5  = \n', np.dot(v1,5), '\n')

m1 = np.array([[5,12,6],[-3,0,14]])
print('m1 is the matric \n', m1, '\n')
m2 = np.array([[9,8],[1,3],[7,-5]])
print('m2 is the matric \n', m2, '\n')

print('m1 x m2  = \n', np.dot(m1,m2), '\n')