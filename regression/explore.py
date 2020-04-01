import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_variable_pairs(df):
    sns.pairplot(df, kind="reg")
    plt.show();

def months_to_years(tenure_months, df):
    df['tenure_years'] = round(tenure_months/12)
    return df

def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    f, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
    plt.figure()
    sns.boxplot(x= categorical_var, y= continuous_var, data=df, ax=axes[0])
    plt.figure()
    sns.swarmplot(x= categorical_var, y= continuous_var, data=df)
    plt.figure()
    sns.barplot(x= categorical_var, y= continuous_var, data=df)