# 4. Design a TLN for binary inputs

import numpy as np

class TLN:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = learning_rate

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(i) for i in linear_output])

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            for i in range(len(X)):
                linear_output = np.dot(X[i], self.weights) + self.bias
                prediction = self.activation_function(linear_output)
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X[i]
                self.bias += self.learning_rate * error

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Binary inputs
y = np.array([0, 0, 0, 1])  # Output for logical AND operation

tln = TLN(input_size=2)
tln.train(X, y, epochs=10000)

final_output = tln.predict(X)
final_output
