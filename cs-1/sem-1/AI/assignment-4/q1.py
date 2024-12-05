# 1. Design a Neural Network that implements a 2 input AND gate

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

np.random.seed(1)
weights = np.random.rand(2, 1)
bias = np.random.rand(1)

learning_rate = 0.1

for epoch in range(10000):
    linear_output = np.dot(X, weights) + bias
    output = sigmoid(linear_output)
    error = y - output
    d_output = error * sigmoid_derivative(output)
    weights += np.dot(X.T, d_output) * learning_rate
    bias += np.sum(d_output) * learning_rate

final_output = sigmoid(np.dot(X, weights) + bias)
final_output
