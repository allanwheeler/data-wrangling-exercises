import pandas as pd

transactions = pd.read_csv('./input/pd-2023-wk2-transactions.csv')
codes = pd.read_csv('./input/pd-2023-wk2-swift-codes.csv')

# i want to take df['Sort Code'] and remove hyphen
transactions['Sort Code'] = transactions['Sort Code'].str.replace('-','')

# join transactions and codes on transactions['Bank'] and codes['Bank']
transactions = transactions.merge(codes, on='Bank')

transactions.head()
