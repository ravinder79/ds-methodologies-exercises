import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_variable_pairs(df):
    """Takes a DataFrame and all of the pairwise relationships along with the regression line for each pair"""
    sns.pairplot(df, kind="reg",plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
    plt.show();

def months_to_years(tenure_months, df):
    """returns the dataframe with a new feature tenure_years"""
    df['tenure_years'] = round(tenure_months/12)
    return df

def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    """outputs 3 different plots for plotting a categorical variable with a continuous variable"""
    f, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
    plt.figure()
    sns.boxplot(x= categorical_var, y= continuous_var, data=df, ax=axes[0])
    plt.figure()
    sns.swarmplot(x= categorical_var, y= continuous_var, data=df)
    plt.figure()
    sns.barplot(x= categorical_var, y= continuous_var, data=df)