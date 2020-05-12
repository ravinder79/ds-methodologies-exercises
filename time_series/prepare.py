import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt


def read_convert_datetime():
    """ Read Data from CSV and set datetime as index and parse dates columns"""
    df = pd.read_csv('all_data.csv',index_col = 0, parse_dates = True)
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    return df

def set_index_store(df):
    df = df.sort_values('sale_date').set_index('sale_date')
    return df

def add_month_week(df):
    df['day_of_week'] = df.index.day_name()
    df['month'] = df.index.month
    return df

def sales_total(df):
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def sales_diff(df):
    df['sales_diff'] = df.sales_total.diff(1)
    return df

def plot_hist_store(df):
    fig, ax = plt.subplots(1, 2)

    ax[0].hist(df['sale_amount']) 
    ax[0].set_xlabel('Sale Amount')

    ax[1].hist(df['item_price'])
    ax[1].set_xlabel('Item Price')
    plt.tight_layout()

def prepare_store_data():
    df = read_convert_datetime()
    df = set_index_store(df)
    df = add_month_week(df)
    df = sales_total(df)
    df = sales_diff(df)
    plot_hist_store(df)
    return df


## OPS German data 

def read_convert_DT():
    power = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    power['Date'] = pd.to_datetime(power['Date'])
    return power

def set_index_ops(df):
    df = df.sort_values('Date').set_index('Date')
    return df

def add_month_year(df):
    df['month'] = df.index.month
    df['year'] = df.index.year
    return df

def plot_hist(power):
    fig, ax = plt.subplots(2, 2)

    ax[0, 0].hist(power['Consumption']) #row=0, col=0
    ax[0,0].set_xlabel('Consumption')

    ax[1, 0].hist(power['Wind']) #row=1, col=0
    ax[1,0].set_xlabel('Wind')

    ax[0, 1].hist(power['Solar']) #row=0, col=1
    ax[0,1].set_xlabel('Solar')

    ax[1, 1].hist(power['Wind+Solar']) #row=1, col=1

    ax[1,1].set_xlabel('Wind+solar')
    plt.tight_layout()

def prepare_ops_data():
    power = read_convert_DT()
    power = set_index_ops(power)
    power = add_month_year(power)
    plot_hist(power)
    return power
