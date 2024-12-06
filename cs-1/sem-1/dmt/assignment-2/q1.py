# Import required libraries
import pandas as pd

# Read the CSV file
file_path = "Students Performance.csv"  # Replace with the correct path to your file
df = pd.read_csv(file_path)

# a. Display the shape of the dataset
print("Shape of the dataset (rows, columns):", df.shape)

# b. Display the top rows of the dataset with their columns
print("\nTop 5 rows of the dataset:")
print(df.head())

# c. Display random rows from the dataset
num_random_rows = 3  # Specify the number of random rows to display
print(f"\n{num_random_rows} Random rows from the dataset:")
print(df.sample(n=num_random_rows))

# d. Display the number of columns and their names
print("\nNumber of columns:", len(df.columns))
print("Column names:", df.columns.tolist())
