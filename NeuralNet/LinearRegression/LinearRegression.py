import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Generate random input to train on
# Try changing observations: 1000 - 1000000
observations = 1000
xs = np.random.uniform(low=-10, high=10, size=(observations,1))
zs = np.random.uniform(-10,10,(observations,1))
generated_inputs = np.column_stack((xs,zs))

# Create the target we will aim at
noise = np.random.uniform(-1,1,(observations,1))
generated_targets = 2*xs - 3*zs + 5 + noise

# save into a tensor friendly file
np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)

# solve with TensorFlow
training_data = np.load('TF_intro.npz')
input_size = 2
output_size = 1
# create layers with kernal(weight) initalizer and bias initializer
model = tf.keras.Sequential([tf.keras.layers.Dense(output_size,
                        kernel_initializer=tf.random_uniform_initializer(minval=-0.1, maxval=0.1),
                        bias_initializer=tf.random_uniform_initializer(minval=-0.1, maxval=0.1))
  ])
# optimizer, learnign rate, and loss
# try cahnging learning rate: 0.0001 - 1
custom_sgd = tf.keras.optimizers.SGD(learning_rate=0.02)
model.compile(optimizer=custom_sgd,loss='mean_squared_error')
# which data to fit and number of itterations
model.fit(training_data['inputs'], training_data['targets'], epochs=100, verbose=2)
model.layers[0].get_weights()
weights = model.layers[0].get_weights()[0]
print('\nWeights:\n', weights, '\n')
bias = model.layers[0].get_weights()[1]
print('Bias:\n', bias, '\n')

# Extract the outputs (make predictions)
model.predict_on_batch(training_data['inputs']).round(1)
training_data['targets'].round(1)

# Plot the data
plt.plot(np.squeeze(model.predict_on_batch(training_data['inputs'])), np.squeeze(training_data['targets']))
plt.xlabel('outputs')
plt.ylabel('inputs')
plt.show()