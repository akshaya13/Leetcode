import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered = set(orders['customerId'])
    never =  customers[ ~ customers['id'].isin(ordered)]
    res = never[['name']].rename(columns={'name': 'Customers'})
    
    return res