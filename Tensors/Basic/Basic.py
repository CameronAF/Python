import numpy as np

# Declaseing scalars, vecotrs, and matrices
# Scalars
s = 5
print('s is the scalar ', s, '\n')

# Vecors
v = np.array([5,-2,4])
print('v is the vector \n', v, '\n')

# Matrices
m = np.array([[5,12,6],[-3,0,14]])
print('m is the matric \n', m, '\n')

# Datatype
print('s is of type ', type(s))
print('v is of type ', type(v))
print('m is of type ', type(m), '\n')

# change s to a scalar array
s = np.array(5)
print('s is now the scalar ', s,' of type ', type(s), '\n')

# Datashape
print('s has the shape ', s.shape)
print('v has the shape ', v.shape)
print('m has the shape ', m.shape, '\n\n')

# Tensor
m1 = np.array([[5,12,6],[-3,0,14]])
print('m1 is the matric \n', m1, '\n')
m2 = np.array([[9,8,7],[1,3,-5]])
print('m1 is the matric \n', m2, '\n')
t = np.array([m1,m2])
print('t is the tensor \n', t)
print('t has the shape ', t.shape, '\n')

t_manual = np.array([[[5,12,6],[-3,0,14]],[[9,8,7],[1,3,-5]]])