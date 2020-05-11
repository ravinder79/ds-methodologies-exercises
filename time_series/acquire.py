import pandas as pd
import numpy as np
import requests

def get_items():
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    max_page = data['payload']['max_page']
    df = pd.DataFrame(data['payload']['items'])
    for i in range (1, max_page):
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        #print(data)
        df = pd.concat([df,pd.DataFrame(data['payload']['items'])])
        i = i+1
    return df

def get_stores():
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    df = pd.DataFrame(data['payload']['stores'])
    return df

def get_sales():
    base_url = 'https://python.zach.lol'
    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    max_page = data['payload']['max_page']
    df = pd.DataFrame(data['payload']['sales'])
    for i in range (1,max_page):
        response = requests.get(base_url + data['payload']['next_page'])
        #print(base_url + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload']['sales'])])
    return df


def get_all_data():
    items = get_items()
    stores = get_stores()
    sales = get_sales()
    sales = sales.rename(columns = {'item': 'item_id', 'store': 'store_id'})
    sales = sales.merge(stores, on= 'store_id')
    sales = sales.merge(items, on = 'item_id')
    sales.to_csv('all_data.csv')
    return sales


def get_power_data():
    data = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    data.to_csv('opsd_germany_daily.csv')
    return data
