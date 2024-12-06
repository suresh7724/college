# Import required libraries
import numpy as np
import pandas as pd

# 1. Get the NumPy version and show NumPy build configuration
# ----------------------------------------------------------------
print("NumPy Version:", np.__version__)
np.show_config()

# 2. Get help on the add function
# ----------------------------------------------------------------
print("\nHelp on np.add function:")
help(np.add)

# 3. Test whether none of the elements of a given array is zero
# ----------------------------------------------------------------
array1 = np.array([1, 2, 3, 4])
array2 = np.array([1, 0, 3, 4])
print("\nArray1:", array1, "\nNone of its elements are zero:", np.all(array1))
print("Array2:", array2, "\nNone of its elements are zero:", np.all(array2))

# 4. Test element-wise finiteness (not infinity or NaN)
# ----------------------------------------------------------------
array3 = np.array([1, np.inf, 3, -np.inf, np.nan])
print("\nArray3:", array3)
print("Element-wise finiteness:", np.isfinite(array3))

# 5. Create element-wise comparisons (greater, greater_equal, less, less_equal)
# ----------------------------------------------------------------
array4 = np.array([5, 10, 15])
array5 = np.array([2, 10, 20])
print("\nElement-wise greater:", np.greater(array4, array5))
print("Element-wise greater_equal:", np.greater_equal(array4, array5))
print("Element-wise less:", np.less(array4, array5))
print("Element-wise less_equal:", np.less_equal(array4, array5))

# 6. Create an array and determine memory size
# ----------------------------------------------------------------
array6 = np.array([1, 7, 13, 105])
print("\nArray6:", array6)
print("Memory size in bytes:", array6.nbytes)

# 7. Create an array of even integers from 30 to 70
# ----------------------------------------------------------------
array7 = np.arange(30, 71, 2)
print("\nEven integers from 30 to 70:", array7)

# 8. Create a 3x3 identity matrix
# ----------------------------------------------------------------
identity_matrix = np.eye(3)
print("\n3x3 Identity matrix:\n", identity_matrix)

# 9. Generate a random number between 0 and 1
# ----------------------------------------------------------------
random_number = np.random.rand()
print("\nRandom number between 0 and 1:", random_number)

# 10. Generate an array of 15 random numbers from a standard normal distribution
# ----------------------------------------------------------------
random_array = np.random.randn(15)
print("\nArray of 15 random numbers from a standard normal distribution:\n", random_array)

# 11. Create a vector and print all values except the first and last
# ----------------------------------------------------------------
vector = np.arange(15, 56)
print("\nVector excluding the first and last elements:\n", vector[1:-1])

# 12. Create a 3x4 array and iterate over it
# ----------------------------------------------------------------
array8 = np.arange(12).reshape(3, 4)
print("\n3x4 Array:\n", array8)
print("Iterating over the array:")
for row in array8:
    print(row)

# 13. Create a vector of length 5 filled with arbitrary integers from 0 to 10
# ----------------------------------------------------------------
random_integers = np.random.randint(0, 11, 5)
print("\nVector of 5 random integers between 0 and 10:", random_integers)

# 14. Convert a NumPy array to a Pandas series
# ----------------------------------------------------------------
d1 = np.array([10, 20, 30, 40, 50])
series = pd.Series(d1)
print("\nConverted Pandas Series:\n", series)

# 15. Get day of month, day of year, week number, and day of week from date strings
# ----------------------------------------------------------------
date_series = pd.Series(['2023-12-01', '2023-12-06', '2024-01-01'])
date_series = pd.to_datetime(date_series)
print("\nDay of month:", date_series.dt.day)
print("Day of year:", date_series.dt.dayofyear)
print("Week number:", date_series.dt.isocalendar().week)
print("Day of week:", date_series.dt.day_name())

# 16. Convert first and last character of each word to uppercase
# ----------------------------------------------------------------
string_series = pd.Series(["numpy python", "pandas tutorial", "data science"])
result = string_series.apply(lambda x: ' '.join([word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in x.split()]))
print("\nModified Series:\n", result)


import pandas as pd
import numpy as np

# 17. Compute minimum, 25th percentile, median, 75th percentile, and maximum of a series
# -----------------------------------------------------------------------------
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Series Statistics:")
print("Minimum:", series.min())
print("25th Percentile:", series.quantile(0.25))
print("Median:", series.median())
print("75th Percentile:", series.quantile(0.75))
print("Maximum:", series.max())

# 18. Compute mean and standard deviation of the data of a given series
# -----------------------------------------------------------------------------
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 3])
print("\nMean and Standard Deviation:")
print("Mean:", data.mean())
print("Standard Deviation:", data.std())

# 19. Compute the Euclidean distance between two given series
# -----------------------------------------------------------------------------
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([5, 4, 3, 2, 1])
euclidean_distance = np.sqrt(((series1 - series2) ** 2).sum())
print("\nEuclidean Distance between Series1 and Series2:", euclidean_distance)

# 20. Create a TimeSeries to display all the Sundays of a given year
# -----------------------------------------------------------------------------
year = 2024
sundays = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31', freq='W-SUN')
print("\nAll Sundays in the year 2024:")
print(sundays)
