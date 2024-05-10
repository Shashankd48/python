# Take a Data set as per your choice, implement and execute on different inputs of K-Means
# clustering algorithm 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Initialize a list to store silhouette scores for different values of K
silhouette_scores = []

# Set range of K values to try
k_values = range(2, 11)

# Iterate over different values of K
for k in k_values:
    # Initialize KMeans clustering algorithm
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    # Fit the model to the data
    kmeans.fit(X)
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(X, kmeans.labels_)
    
    # Append silhouette score to list
    silhouette_scores.append(silhouette_avg)

# Plotting the silhouette scores for different values of K
plt.plot(k_values, silhouette_scores, marker='o')
plt.title('Silhouette Score vs. Number of Clusters (K)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.xticks(k_values)
plt.grid(True)
plt.show()
