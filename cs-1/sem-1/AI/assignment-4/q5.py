# 5. Implement a 3 layer Neural Network using Keras library on a dataset

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Define the dataset
X = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 1], [0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y = np.array([1, 0, 1, 0, 1, 1, 0])  # Actual outputs for the dataset

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to build the model
def build_model():
    model = Sequential()
    model.add(Dense(5, input_dim=3, activation='relu'))  # Hidden layer (5 neurons)
    model.add(Dense(1, activation='sigmoid'))  # Output layer (1 neuron)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Train and evaluate the model for different epochs
epoch_values = [10, 100, 10000]
results = {}

for epochs in epoch_values:
    model = build_model()
    model.fit(X_train, y_train, epochs=epochs, batch_size=1, verbose=0)
    
    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    results[epochs] = accuracy
    print(f"Epochs: {epochs}, Accuracy: {accuracy:.4f}")

# Test the network on input [1, 0, 0]
input_test = np.array([[1, 0, 0]])
prediction = model.predict(input_test)

# Output the prediction
print(f"Prediction for [1, 0, 0]: {prediction[0][0]:.4f}")
