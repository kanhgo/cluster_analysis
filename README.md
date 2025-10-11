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
