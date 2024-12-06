import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = "salary_data.csv"  # Replace with the correct path to your file
df = pd.read_csv(file_path)

# Display the first few rows of the dataset (optional, for checking the data)
print(df.head())

# Prepare the dataset
# Assuming the last column is the target (Salary) and the others are features (e.g., Years of Experience)
X = df.iloc[:, :-1]  # Features (all columns except the last)
y = df.iloc[:, -1]   # Target (Salary column)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate and print the performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Display the model's coefficients (optional)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
