"""
Reference the following for additional explanatory comments:

.../Continuing Education - Lite/Machine Learning Ops/2-DevOps_DataOps_MLOps/
MOD-2_Essential Maths and Data Science/3-Machine Learning and AI in Practice/15-Cluster_Analysis.ipynb

.../Continuing Education - Lite/Machine Learning Ops/PRACTICE_ADD READINGS/
WORKING WITH MULTIPLE PYTHON VERSIONS IN YOUR CODESPACE OR SERVER ENV

"""

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

# Load dataset and identify columns for scaling
df = pd.read_csv("synthetic_transit_data.csv")
df_num = df.drop(columns=["Trip_ID"])

# Scale the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_num)

"""
EXPERIENCED COMPATABILITY ISSUES WITH yellowbrick IN THE DEFAULT ENVIRONMENT (PYTHON 3.12.x)
I.E. ONE OF ITS DEPENDENCIES (DISTUTILS) WAS NOT COMPATABLE WITH PYTHON 3.12.x
UTILIZED PYENV TO INSTALL AND MAKE ACCESSIBLE, ADDITIONAL PYTHON VERSIONS (3.10.x).
CREATED A VIRTUAL ENVIRONMENT WITH PYTHON 3.10.x AND INSTALLED THE REQUIRED PACKAGES.

"""

# Use Elbow method to determine optimal number of clusters (k)
from yellowbrick.cluster import KElbowVisualizer
import matplotlib.pyplot as plt
# Instantiate the clustering model and visualizer
model = KMeans(random_state=42)
visualizer = KElbowVisualizer(model, k=(2,10))
# Fit the data to the visualizer
visualizer.fit(df_scaled)
# Finalize and render the figure
visualizer.poof()
# Save the elbow method plot
plt.savefig("elbow_method_YB.png")
# Close the plot object to ensure subsequent plots draw on completely clean canvas. Frees up memory.
plt.close()


# Further evaluate the optimal number of clusters using Silhouette Analysis
from yellowbrick.cluster import SilhouetteVisualizer
# Create a KMeans instance with the suggested optimal number of clusters (i.e. 3)
model = KMeans(n_clusters=3, random_state=42)
# Create a SilhouetteVisualizer instance
visualizer = SilhouetteVisualizer(model)
# Fit the visualizer to the scaled data
visualizer.fit(df_scaled)
# Finalize and render the figure
visualizer.poof()
# Save the silhouette analysis plot
plt.savefig("silhouette_analysis.png")
# Close the plot object to ensure subsequent plots draw on completely clean canvas. Frees up memory.
plt.close()

"""
REVIEW OF INITIAL DIAGNOSTICS
The Elbow Method plot suggests that the optimal number of clusters (k) is 4 despite the synthetic data 
being generated with 3 intentional clusters that match the "business logic". 
This maybe indicative of an unintentional sub-cluster within one of the original clusters.

The Silhouette Analysis plot for k=3 shows that all samples have a positive silhouette score. 
A score above 0.4 is generally considered decent for real-world data. 

NEXT STEPS
1. Experiment with k=4 in the Silhouette Analysis to see if it improves the average silhouette score.
2. Use the KMeans model with the chosen k to fit the data and predict cluster assignments.
3. Analyze the characteristics of each cluster to understand their differences and similarities.

"""

# Create a KMeans instance with 4 clusters
model = KMeans(n_clusters=4, random_state=42)
# Create a SilhouetteVisualizer instance
visualizer = SilhouetteVisualizer(model)
# Fit the visualizer to the scaled data
visualizer.fit(df_scaled)
# Finalize and render the figure
visualizer.poof()
# Save the silhouette analysis plot
plt.savefig("silhouette_analysis_k4.png")
# Close the plot object to ensure subsequent plots draw on completely clean canvas. Frees up memory.
plt.close()

"""
The Silhouette Analysis for k=4 shows a siignificant decrease in the average score to approximately 0.34 from 
0.42 (with k=3). This suggests that k=3 is a better choice for this dataset, aligning with the original
data generation logic.
An intercluster distance map could be useful to further evaluate the cluster separation.
"""

from yellowbrick.cluster import InterclusterDistance

# Instantiate the clustering model and visualizer for three clusters
visualizer = InterclusterDistance(KMeans(n_clusters=3, random_state=42))
# Fit the visualizer to the scaled data
visualizer.fit(df_scaled)
# Finalize and render the figure
visualizer.poof()
# Save the intercluster distance analysis plot
plt.savefig("ICD_analysis_k3.png")
# Close the plot object to ensure subsequent plots draw on completely clean canvas. Frees up memory.
plt.close()

"""
Intercluster Distance Map for k=3 shows that the clusters are distinct and well separated with no overlap.
The proportions reflect the original data generation logic.
"""

## ELBOW METHOD FROM SCRATCH (WITHOUT YELLOWBRICK; PYTHON 3.12 COMPATIBLE))
# import matplotlib.pyplot as plt

# distortions = []  # List to hold distortion values (distortion is a measure of how tightly the clusters are packed)
# for i in range(1, 11):  # Testing k values from 1 to 10
#     km = KMeans(n_clusters=i,  # Number of clusters
#             init='k-means++', # Method for initializing centroids. 'k-means++' selects initial cluster centers that are far away from each other.
#             n_init=10,  # Number of times the k-means algorithm will be run with different centroid seeds. Defaults to 10.
#             max_iter=300, # Maximum number of iterations for a single run of the k-means algorithm. Defaults to 300.
#             random_state=42)
#     km.fit(df_scaled) # Fit the KMeans model to the scaled data
#     distortions.append(km.inertia_)

# plt.plot(range(1,11), distortions, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('Distortion')
# plt.title("Elbow Method - Cluster Analysis")
# # Use the following to display the plot in an interactive window or if working in a Jupyter notebook
# #plt.show()
# plt.savefig("elbow_method_MAN.png")