"""Reusable PCA utilities for Lab 2.

During Task 2.4, move the functions developed in the notebook into this file.
"""

# TODO: add the imports required by your functions.
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# TODO: move run_pca() here.
def run_pca(dataframe, feature_names, n_components):
    dataframe_cleaned = dataframe[feature_names].dropna() # Clean the dataframe and select only the information of the features chosen
    feature_values = dataframe_cleaned.values             # Retrive only the values of each features

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(feature_values)  # Scale values before runing pca
    pca = PCA(n_components)
    transformed_values = pca.fit_transform(scaled_values) # New values for each features after runing pca
    return pca
# TODO: move plot_explained_variance() here.
def plot_explained_variance(pca_model):
    explained_variance_ratio = pca_model.explained_variance_ratio_
    plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
    plt.xlabel("Principal component")
    plt.ylabel("Explained variance ratio")
    plt.title("PCA explained variance")
    plt.xticks(range(1, len(explained_variance_ratio) + 1))
    plt.show()