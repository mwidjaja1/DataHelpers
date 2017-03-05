#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:41:40 2017

@author: Matthew
"""

import pandas as pd


def data(in_file):
    """ Loads CSV file as Pandas DataFrame. """
    data = pd.read_csv(in_file, header=0, index_col=0)
    return data


def split(data, target_col):
    """ Splits data into a feature & target set, based on the target_col """
    cols = [x for x in data.columns if x != target_col]
    return data[cols], data[target_col]


def map_string(data, dict_map):
    """ Replaces strings with an int from a dictionary map. The dictionary map
        should be {<col_name>: {<find_value>: <replace_int>} ...} """
    for col in dict_map:
        data[col] = data[col].apply(lambda x: dict_map[col][x])
    return data


def classify(data, column):
    """ Splits a DataFrame into multiple DataFrames, saved in a dict, where
        each DataFrame consists of rows which have identical column values """
    classify_data = {str(x): pd.DataFrame() for x in data[column].unique()}
    for x in classify_data:
        classify_data[str(x)] = data[data[column] == int(x)]
    return classify_data


def plot_feature(data, target):
    """ Tries to scatter plot all features against the target """
    for column in [x for x in data.columns if x != target]:
        try:
            data.plot.scatter(y=target, x=column)
        except Exception:
            print('Could not plot {}'.format(column))
