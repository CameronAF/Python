import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random input to train on
# Try changing observations: 1000 - 1000000
observations = 1000

xs = np.random.uniform(low=-10, high=10, size=(observations,1))
zs = np.random.uniform(-10,10,(observations,1))

inputs = np.column_stack((xs,zs))
print('Shape of inputs:\n', inputs.shape, '\n')

# Create the target we will aim at
noise = np.random.uniform(-1,1,(observations,1))
targets = 2*xs - 3*zs + 5 + noise
print('Shape of targets:\n', targets.shape, '\n')

# Plot the training data
targets = targets.reshape(observations,)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, zs, targets)
ax.set_xlabel('xs')
ax.set_ylabel('zs')
ax.set_zlabel('Targets')
ax.view_init(azim=100)
plt.show()
targets = targets.reshape(observations,1)

# Initialize variables
init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(2,1))
biases = np.random.uniform(-init_range, init_range, size=1)
print('Weights:\n', weights, '\n')
print('Biases:\n', biases, '\n')

# Set Learning rate
# try cahnging learning rate: 0.0001 - 1
learning_rate = 0.02

# Train the Model
print('Loss:')
for i in range(100):
  # calculates output for given weights and biases
  outputs = np.dot(inputs,weights) + biases
  deltas = outputs - targets
  # calculates the loss function that commpares the outputs to the targets
  loss = np.sum(deltas ** 2) / 2 / observations
  print(loss)
  deltas_scaled = deltas / observations
  # update weights and biases following gradient decent methodology 
  weights = weights - learning_rate * np.dot(inputs.T,deltas_scaled)
  biases = biases - learning_rate * np.sum(deltas_scaled)

# Print weights and biases and see if we have worked correctly
print('\nWeights:\n', weights, '\n')
print('Biases:\n', biases, '\n')

plt.plot(outputs, targets)
plt.xlabel('outputs')
plt.ylabel('targets')
plt.show()