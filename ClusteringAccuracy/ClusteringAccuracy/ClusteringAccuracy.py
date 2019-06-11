import numpy as np
import itertools
try:
	# Python 2
	from itertools import izip
except ImportError:
	# Python 3
	izip = zip


max1 = 0
max2 = 0
count = 0
#find the max value of cluster and count
with open('clustering_result.txt') as f:
	for line in f:
		val = int(line.strip())
		if val > max1:
			max1 = val
		count += 1
#find the max values of classes
with open('data_label.txt') as f:
	for line in f:
		val = int(line.strip())
		if val > max2:
			max2 = val
#make a 2D array of size cluster and class max
matrix = np.zeros((max1,max2)) #cluster - row, class - column
#read text files and populate matrix
with open('clustering_result.txt') as f1, open('data_label.txt') as f2:
	for line1, line2 in zip(f1,f2):
		val1 = int(line1.strip())
		val2 = int(line2.strip())
		matrix[(val1-1)][(val2-1)] += 1
print("Clustering Matrix: row - cluster indicator, column - class label")
print(matrix)
#calculate max permutation submation
num_perm = 0
max_sum = 0
best_item = []
for p in itertools.permutations(range(max2)): #check all permutations of classes
	num_perm += 1
	sum = 0
	for i in range(0,max1): #sum of current permutation
		sum = sum + matrix[i,p[i]]
	if sum > max_sum: #is best permutation?
		max_sum = sum
		best_item = p
#print results
print ("%s permutations found" %num_perm)
print ("%s max sum of permutation"%max_sum)
for i in range (0,max1):
	if i == 0:
		print ("[(%s, %s), " % (i, (best_item[i]+1)), end='')
	else: 
		if i == (max1-1):
			print ("(%s, %s)]" % (i, (best_item[i]+1)))
		else:
			print ("(%s, %s), " % (i, (best_item[i]+1)), end='')
print ("Clustering accuracy is %1.4f" % (max_sum/count))