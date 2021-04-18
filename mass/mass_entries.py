import pandas as pd
import numpy as np
import scipy
from sklearn.neighbors import NearestCentroid


def get_class_labels_and_freq(labels):
    class_labels, counts_elements = np.unique(labels, return_counts=True)
    return {class_label: count_elements for class_label,count_elements in zip(class_labels, counts_elements)}

def get_centeroids_per_class(features, labels):
    clf = NearestCentroid()
    clf.fit(features, labels)
    centroids = clf.centroids_
    class_labels = clf.predict(clf.centroids_)
    return {class_label: centroid for class_label,centroid in zip(class_labels,centroids)}

def get_infos(features, labels, x_q, class_q):
    # Get class labels and the number of instances per class
    labels_and_freq = get_class_labels_and_freq(labels)
    class_labels, instances_per_class = labels_and_freq.keys(), labels_and_freq.values()

    # Get the centroids per class label
    centroids_per_class = get_centeroids_per_class(features, labels)

    # Find the nearest centroid of a different class
    nearest_centroid_distance = min([np.linalg.norm(x_q - item[1]) for item in centroids_per_class.items() if item[0] != class_q])

    # Find the distances btween the current instance and the other instances in the same and different class
    same_class_data = [data for data,label in zip(features,labels) if label == class_q]
    diff_class_data = [data for data,label in zip(features,labels) if label != class_q]

    same_class_dist = [np.linalg.norm(x_q - x_j) for x_j in same_class_data]
    diff_class_dist = [np.linalg.norm(x_q - x_j) for x_j in diff_class_data]
    total_dist = sorted([(np.linalg.norm(x_q - x_j), x_j, label) for x_j,label in zip(features,labels)], key=lambda x: x[0])[1:]

    # Calculate imbalance ratio
    n_maj, n_min = max(instances_per_class), min(instances_per_class)

    # Calculate de pci`s
    pcis = {"pc" + str(i): 0 for i in range(1,11)}
    pcis["pc1"] = n_maj / n_min
    pcis["pc2"] = labels_and_freq[class_q]
    pcis["pc3"] = n_maj
    pcis["pc4"] = sum(instances_per_class)
    pcis["pc5"] = np.linalg.norm(x_q - centroids_per_class[class_q])
    pcis["pc6"] = nearest_centroid_distance
    pcis["pc7"] = sum(same_class_dist)
    pcis["pc8"] = sum(diff_class_dist)
    pcis["pc9"] = sum([1 if item[2] == class_q else 0 for item in total_dist[0:7]])
    pcis["pc10"] = sum([1 if item[2] != class_q else 0 for item in total_dist[0:7]])

    return pcis
