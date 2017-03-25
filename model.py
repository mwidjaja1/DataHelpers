#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper Functions to model using Scikit-Learn
"""

import matplotlib.pyplot as plt
from sklearn import cluster, linear_model


def kmeans(train_data, clusters=8):
    """ Performs a K-Means clustering algorithm on data.

        Inputs:
        train_data: A series or list of tuples of (x, y) points
        clusters: How many clusters to create [Default = 8]

        Outputs:
        cluster_data: A dict where each cluster's center is a key and its
                      value is a list of all points connected to that center.
    """
    # Performs K-Means Clustering
    kmeans = cluster.KMeans(n_clusters=clusters,
                            precompute_distances=True,
                            n_jobs=-2)
    if isinstance(train_data, list):
        kmean_data = kmeans.fit(train_data)
    else:
        kmean_data = kmeans.fit(train_data.tolist())

    # Identifies centers for each cluster
    centers = [(x[0], x[1]) for x in kmean_data.cluster_centers_]
    center_per_pt = kmean_data.labels_.tolist()

    # Identifies which center each data point is connected to
    cluster_data = {center: 0 for center in centers}
    for idx, centers in enumerate(centers):
        cluster_data[centers] = center_per_pt.count(idx)
    return cluster_data


def linear_regression(train_feature, train_target, test_feature, test_target):
    """ Perorms linear regression on a training data set and then tests it
        on the test data set """
    # Performs Linear Regression
    alg = linear_model.LinearRegression()
    alg.fit(train_feature, train_target)

    # Shows Coefficients
    print('\nCoefficient:')
    for pair in zip(test_feature.columns, alg.coef_):
        print('{}: {:.2f}'.format(*pair))

    # Tests regression against the test data
    test_prediction = alg.predict(test_feature)

    # Plots Regression Difference
    plt.figure()
    plt.scatter(test_target, test_prediction)
    plt.show()
    return test_prediction
