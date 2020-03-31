
import pandas as pd
import numpy as np
import sklearn.preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def split_my_data(X, y, train_pct):

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = train_pct, random_state=123)
    return X_train, X_test, y_train, y_test

def standard_scaler(X_train, X_test):
    scaler = sklearn.preprocessing.StandardScaler()
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    scaler.fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train),columns=X_train.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

    return  scaler, X_train_scaled,  X_test_scaled

def scale_inverse(X_train_scaled, X_test_scaled):
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(X_train_scaled)
    train_unscaled = pd.DataFrame(scaler.inverse_transform(X_train_scaled), columns=X_train_scaled.columns.values).set_index([X_train_scaled.index.values])
    test_unscaled = pd.DataFrame(scaler.inverse_transform(X_test_scaled), columns=X_test_scaled.columns.values).set_index([X_test_scaled.index.values])
    return  scaler, X_train_scaled,  X_test_scaled


def uniform_scaler(X_train, X_test):
    scaler = sklearn.preprocessing.QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns.values).set_index([X_train.index.values])
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns.values).set_index([X_test.index.values])
    return scaler, X_train_scaled, X_test_scaled


def gaussian_scaler(X_train, X_test):
    scaler = sklearn.preprocessing.PowerTransformer(method='box-cox', standardize=False, copy=True).fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns.values).set_index([X_train.index.values])
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns.values).set_index([X_test.index.values])
    return scaler, X_train_scaled, X_test_scaled

def min_max_scaler(X_train, X_test):
    scaler = sklearn.preprocessing.MinMaxScaler(copy=True, feature_range=(0,1)).fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns.values).set_index([X_train.index.values])
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns.values).set_index([X_test.index.values])
    return scaler, X_train_scaled, X_test_scaled

def iqr_robust_scaler(X_train, X_test):
    scaler = sklearn.preprocessing.RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns.values).set_index([X_train.index.values])
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns.values).set_index([X_test.index.values])
    return scaler, X_train_scaled, X_test_scaled