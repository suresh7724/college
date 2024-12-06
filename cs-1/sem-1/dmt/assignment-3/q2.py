# Import required libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load the dataset
file_path = "Market_Basket_Optimisation.csv"  # Replace with your dataset path
df = pd.read_csv(file_path, header=None)

# Prepare the dataset for Apriori
# Convert transactions into a list of lists
transactions = df.apply(lambda row: row.dropna().tolist(), axis=1).tolist()

# Convert transactions to a one-hot encoded DataFrame
unique_items = set(item for sublist in transactions for item in sublist)
one_hot_encoded = pd.DataFrame(
    [{item: (item in transaction) for item in unique_items} for transaction in transactions]
)

# Apply Apriori algorithm
min_support = 0.004  # Example: Adjust as needed
frequent_itemsets = apriori(one_hot_encoded, min_support=min_support, use_colnames=True)

# Generate association rules
min_confidence = 0.2  # Example: Adjust as needed
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
