import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
file_path = "iris.csv"  # Replace with the correct path to your file
df = pd.read_csv(file_path)

# a. Bar plot for species frequency
species_counts = df['species'].value_counts()
species_counts.plot(kind='bar', color=['blue', 'green', 'orange'])
plt.title('Frequency of Iris Species')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.show()

# b. Histogram for species
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.hist(subset['sepal_length'], alpha=0.7, label=f"{species} (Sepal Length)")
    plt.hist(subset['sepal_width'], alpha=0.7, label=f"{species} (Sepal Width)")

plt.title('Histogram of Iris Species')
plt.xlabel('Measurement Values')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()
