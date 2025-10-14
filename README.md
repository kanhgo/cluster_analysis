# cluster_analysis
Application of k-means clustering to a synthetic dataset

### About the dataset
This Python script creates a pre-defined nunber of records that are intentionally clustered around three typical travel patterns: Morning Commute, Mid-day Errands, and Late Night Transit. This structure makes it ideal for practicing K-Means clustering, as the model is expected to naturally discover the three underlying groups.

### Managing package (yellowbrick) vs python environment compatibility issues
If working in codespace or server environment:

1. If needed, install pyenv
```python
   sudo apt install pyenv
```
   
2. If the above does not work, pyenv must be first downloaded, followed by configuration of the shell:
```python
   curl https://pyenv.run | bash
```
   Add the initialization code:
```python
   echo -e 'export PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc
```
   Restart the Terminal:
```python
   source ~/.bashrc
```
3. Install the required python version
```python
   pyenv install 3.10
```
   (Use ```python_pyenv versions``` to get the exact version of python installed in the hidden directory)
   
5. Create the virtual environment with required python version
```python
   ~/.pyenv/versions/3.10.19/bin/python3.10 -m venv .venv
```

### Diagnistics and Analysis
K-means is one of the most popular forms of clustering - an unsupervised machine learning technique.

Diagnostic tools considered:

- Elbow plots
- Silhouette analysis
- Intercluster distance mapping

Elbow plots aid in determining the optimal number of clusters. 
* The Elbow Plot visualizes how distortion/ inertia changes as you increase the number of clusters (K). The "elbow" point is where the benefit (the decrease in distortion) no longer justifies the complexity (the increase in K). Distortion measures the intracluster variation (the spread of points within their own cluster).

Silhouette Analysis provides a measure of how similar an object is to its own cluster compared to other clusters.  
* It allows you to assess the density of the clusters. It is an internal validation technique. Silhouette analysis is executed for different values of K, to further support identification of the optimal number of clusters.

Intercluster distance analysis visualizes the relationships and separation between the clusters themselves.
* The physical distance between the circles on this map roughly approximates to the actual dissimilarity (Euclidean distance) between the cluster centroids in the original, full-dimensional feature space. Therefore, the further apart two circles are, the more distinct and well-separated those two clusters are.

KMeans model was used with the chosen k to fit the data and predict cluster assignments.

This was followed by exploratory analysis of the characteristics of each cluster to understand their differences and similarities.