import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# === LOAD DATA ===
df = pd.read_csv('final_data.csv')
df = df.dropna(subset=['latitude', 'longitude'])

# Prepare data
coords = df[['latitude', 'longitude']].values

# === ELBOW METHOD TO CHOOSE k ===
inertia = []
k_range = range(1, 21)  # Try k = 1 to 20

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(coords)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8,5))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.title('Elbow Method for Choosing k')
plt.grid(True)
plt.savefig('elbow_plot.png', dpi=300, bbox_inches='tight')
print("✅ Elbow plot saved as 'elbow_plot.png'")

# === K-MEANS CLUSTERING WITH YOUR CHOSEN k ===
k = 5# <-- You chose 15 clusters
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(coords)
kmeans.cluster_centers_


# === GET CENTROIDS ===
centroids = kmeans.cluster_centers_
centroids_df = pd.DataFrame(centroids, columns=['latitude', 'longitude'])
centroids_df.to_csv('cluster_centroids.csv', index=False)
print("✅ Cluster centroids saved to 'cluster_centroids.csv'")


# Add cluster labels back to dataframe
df['cluster'] = kmeans.labels_

# === PLOT CLUSTERS ===
plt.figure(figsize=(10,6))
plt.scatter(df['longitude'], df['latitude'], c=df['cluster'], cmap='viridis', s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'K-Means Clustering of Coordinates (k={k})')
plt.grid(True)
plt.savefig('kmeans.png', dpi=300, bbox_inches='tight')
print("✅ Cluster plot saved as 'kmeans.png'")


print("📍 Cluster Centers:")
print(centroids_df)
