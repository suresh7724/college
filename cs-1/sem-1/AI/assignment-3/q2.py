# 2. Implement Naïve Bayes Models.

from collections import defaultdict
import math

class NaiveBayes:
    def __init__(self):
        self.classes = None
        self.class_probs = {}
        self.feature_probs = defaultdict(lambda: defaultdict(float))

    def fit(self, X, y):
        self.classes = set(y)
        total_samples = len(y)
        
        for cls in self.classes:
            cls_count = y.count(cls)
            self.class_probs[cls] = cls_count / total_samples
            
            cls_samples = [X[i] for i in range(len(y)) if y[i] == cls]
            total_features = len(cls_samples) * len(cls_samples[0])
            
            feature_counts = defaultdict(int)
            for sample in cls_samples:
                for feature in sample:
                    feature_counts[feature] += 1
            
            for feature in feature_counts:
                self.feature_probs[cls][feature] = feature_counts[feature] / total_features

    def predict(self, X):
        predictions = []
        for sample in X:
            class_scores = {}
            for cls in self.classes:
                class_scores[cls] = math.log(self.class_probs[cls])
                for feature in sample:
                    if feature in self.feature_probs[cls]:
                        class_scores[cls] += math.log(self.feature_probs[cls][feature])
                    else:
                        class_scores[cls] += math.log(1e-6)  # Smoothing for unseen features
            
            predictions.append(max(class_scores, key=class_scores.get))
        return predictions

# Example dataset
X = [['sunny', 'hot', 'high', 'weak'],
     ['sunny', 'hot', 'high', 'strong'],
     ['overcast', 'hot', 'high', 'weak'],
     ['rain', 'mild', 'high', 'weak'],
     ['rain', 'cool', 'normal', 'weak'],
     ['rain', 'cool', 'normal', 'strong'],
     ['overcast', 'cool', 'normal', 'strong'],
     ['sunny', 'mild', 'high', 'weak'],
     ['sunny', 'cool', 'normal', 'weak'],
     ['rain', 'mild', 'normal', 'weak'],
     ['sunny', 'mild', 'normal', 'strong'],
     ['overcast', 'mild', 'high', 'strong'],
     ['overcast', 'hot', 'normal', 'weak'],
     ['rain', 'mild', 'high', 'strong']]

y = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

# Train the model
nb = NaiveBayes()
nb.fit(X, y)

# Predict using the model
test_data = [['sunny', 'cool', 'high', 'strong'], ['overcast', 'hot', 'normal', 'weak']]
predictions = nb.predict(test_data)
predictions
