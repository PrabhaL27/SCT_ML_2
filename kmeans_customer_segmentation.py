import os
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

os.environ["LOKY_MAX_CPU_COUNT"] = "4"
warnings.filterwarnings("ignore", category=UserWarning)

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'AnnualIncome': [15, 16, 17, 18, 19, 50, 52, 53, 85, 86],
    'SpendingScore': [39, 81, 6, 77, 40, 85, 20, 90, 99, 55]
}


df = pd.DataFrame(data)
print("📊 Sample Customer Data:\n", df)


X = df[['AnnualIncome', 'SpendingScore']]


inertia = []
K = range(1, 11)
for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    inertia.append(km.inertia_)


plt.figure(figsize=(8, 4))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method to Find Optimal k')
plt.grid(True)
plt.show()


kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='AnnualIncome', y='SpendingScore', hue='Cluster', palette='Set2', s=100)
plt.title('Customer Segments Based on Purchase History')
plt.xlabel('Annual Income (in $1000s)')
plt.ylabel('Spending Score (1–100)')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()


print("\n📌 Cluster Centers:")
for idx, center in enumerate(kmeans.cluster_centers_):
    print(f"Cluster {idx}: AnnualIncome = {center[0]:.2f}, SpendingScore = {center[1]:.2f}")
