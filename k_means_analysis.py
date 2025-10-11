"""
Reference the following for additional explanatory comments:

.../Continuing Education - Lite/Machine Learning Ops/2-DevOps_DataOps_MLOps/
MOD-2_Essential Maths and Data Science/3-Machine Learning and AI in Practice/15-Cluster_Analysis.ipynb

.../Continuing Education - Lite/Machine Learning Ops/PRACTICE_ADD READINGS/
WORKING WITH MULTIPLE PYTHON VERSIONS IN YOUR CODESPACE OR SERVER ENV

"""

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
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
model = KMeans()
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
# Create a KMeans instance with the optimal number of clusters (e.g., 3)
model2 = KMeans(n_clusters=3, random_state=42)
# Create a SilhouetteVisualizer instance
visualizer2 = SilhouetteVisualizer(model2)
# Fit the visualizer to the scaled data
visualizer2.fit(df_scaled)
# Finalize and render the figure
visualizer2.poof()
# Save the silhouette analysis plot
plt.savefig("silhouette_analysis.png")
# Close the plot object to ensure subsequent plots draw on completely clean canvas. Frees up memory.
plt.close()

# # Create a pipeline that first standardizes the data then applies K-Means
# pipeline = make_pipeline(StandardScaler(), KMeans(n_clusters=3, random_state=42))
# # Fit the pipeline to the numerical data
# kmeans = pipeline.fit(df_num)


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
# plt.savefig("elbow_method.png")