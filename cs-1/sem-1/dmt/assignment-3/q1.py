from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Load the dataset
file_path = "groceries.csv"  # Replace with the correct file path
df = pd.read_csv(file_path, header=None)

# Prepare the dataset for Apriori
# Convert transactions to one-hot encoded DataFrame
transactions = df.stack().groupby(level=0).apply(list)
unique_items = set(item for sublist in transactions for item in sublist)
one_hot_encoded = pd.DataFrame(
    [{item: (item in transaction) for item in unique_items} for transaction in transactions]
)

# Apply Apriori algorithm
frequent_itemsets = apriori(one_hot_encoded, min_support=0.004, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.2)

# Apply additional filtering
filtered_rules = rules[
    (rules['lift'] >= 3) & 
    (rules['confidence'] >= 0.2) & 
    (rules['antecedents'].apply(len) >= 2)
]

# Display support and confidence of each rule
print("Support and Confidence for each rule:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Display filtered rules with min_support=0.004, min_confidence=0.2, min_lift=3, min_length=2
print("\nFiltered Rules:")
print(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
