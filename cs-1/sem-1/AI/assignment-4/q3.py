# 3. Design a Perceptron for bipolar inputs

import numpy as np

def activation_function(x):
    return np.where(x >= 0, 1, -1)

X = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])  # Bipolar inputs (-1 and 1)
y = np.array([-1, -1, -1, 1])  # Bipolar output for AND gate

np.random.seed(1)
weights = np.random.rand(2, 1)  # Random initialization of weights
bias = np.random.rand(1)

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    for i in range(len(X)):
        linear_output = np.dot(X[i], weights) + bias
        prediction = activation_function(linear_output)
        error = y[i] - prediction
        weights += learning_rate * error * X[i].reshape(-1, 1)
        bias += learning_rate * error

final_output = np.array([activation_function(np.dot(x, weights) + bias) for x in X])
final_output
