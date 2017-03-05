#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:06:00 2017

@author: Matthew
"""

import matplotlib.pyplot as plt
from sklearn import ensemble, linear_model


def features(data_feature, data_target):
    """ Depricated? Does Feature Importance but plot function in load.py
        seems better """
    features = {}
    model = ensemble.RandomForestRegressor(n_estimators=3)
    model.fit(data_feature, data_target)
    for idx, column in enumerate(data_feature.columns):
        features[column] = model.feature_importances_[idx]
    return features


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
