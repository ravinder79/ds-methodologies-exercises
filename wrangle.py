#As a customer analyst, I want to know who has spent the most money with us over their lifetime. I have monthly charges and tenure,
# so I think I will be able to use those two attributes as features to estimate total_charges. 
# I need to do this within an average of $5.00 per customer.

# 1. Acquire customer_id, monthly_charges, tenure, and total_charges from telco_churn database for all customers with a 2 year contract.

import pandas as pd
import numpy as np
import env

def wrangle_telco():
    customers = pd.read_sql("SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 2", env.get_db_url('telco_churn'))

    customers['total_charges'] = customers['total_charges'].str.strip()
    customers = customers.replace(r'^\s*$', np.nan, regex=True)
    customers = customers.dropna()
    customers['total_charges'] = customers['total_charges'].astype(float)
    return customers
    
#print(customers.sort_values(by='total_charges'))
#print(f' Shape = {customers.shape}')
#print(f'Describe = {customers.describe()}')