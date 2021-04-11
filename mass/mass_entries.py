import pandas as pd
import numpy as np
from sklearn.neighbors import NearestCentroid


def get_class_labels(dataset):
    class_labels = dataset[dataset.columns[-1]].unique()
    return class_labels

def get_centeroids_per_class(dataset):
    X, y = dataset.iloc[:, 0:-1].to_numpy(), dataset.iloc[:,-1].squeeze().to_numpy()

    clf = NearestCentroid()
    clf.fit(X, y)
    centroids = clf.centroids_
    class_labels = clf.predict(clf.centroids_)
    return {class_label: centroid for class_label,centroid in zip(class_labels,centroids)}

def get_instances_per_class(dataset, class_labels):
    instances_per_class = {class_label: 0 for class_label in class_labels}
    
    for class_label in class_labels:
        n_instances = len(dataset[dataset.iloc[:,-1] == class_label].index) 
        instances_per_class[class_label] = n_instances
    return instances_per_class

def get_infos(dataset, x_i, class_i):
    # Get class labels
    class_labels = get_class_labels(dataset)

    # Get the number of instances per class label
    instances_per_class = get_instances_per_class(dataset, class_labels)

    # Get the centroids per class label
    centroids_per_class = get_centeroids_per_class(dataset)

    # Find the nearest centroid
    nearest_centroid_distance = min([np.linalg.norm(x_i - item[1]) for item in centroids_per_class.items() if item[0] != class_i])

    # Find the distances from the current instance for the other instances in the same and different class
    same_class_data = dataset[dataset.iloc[:,-1] == class_i].values
    diff_class_data = dataset[dataset.iloc[:,-1] != class_i].values
    same_class_dist = [np.linalg.norm(x_i - x_j[:-1]) for x_j in same_class_data]
    diff_class_dist = [np.linalg.norm(x_i - x_j[:-1]) for x_j in diff_class_data]
    total_dist = sorted([(np.linalg.norm(x_i - x_j[:-1]), x_j) for x_j in dataset.values], key=lambda x: x[0])[1:]

    # Calculate imbalance ratio
    n_maj, n_min = max(instances_per_class.values()), min(instances_per_class.values())

    # Calculate de pci`s
    pcis = {"pc"+str(i): 0 for i in range(1,11)}
    pcis["pc1"] = n_maj / n_min
    pcis["pc2"] = instances_per_class[class_i]
    pcis["pc3"] = n_maj
    pcis["pc4"] = sum(instances_per_class.values())
    pcis["pc5"] = np.linalg.norm(x_i - centroids_per_class[class_i])
    pcis["pc6"] = nearest_centroid_distance
    pcis["pc7"] = sum(same_class_dist)
    pcis["pc8"] = sum(diff_class_dist)
    pcis["pc9"] = sum([1 if item[1][-1] == class_i else 0 for item in total_dist[0:7]])
    pcis["pc10"] = sum([1 if item[1][-1] != class_i else 0 for item in total_dist[0:7]])

    return pcis

# # Test
# df = pd.read_csv("datasets/iris/iris.data",header=None)
# get_infos(df, [5.0,3.6,1.4,0.2], "Iris-setosa")