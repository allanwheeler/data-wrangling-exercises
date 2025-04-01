import pandas as pd

# Input the data
df = pd.read_csv('../input/pd-2023-wk1-input.csv')

# Split the Transaction Code to extract the letters at the start of the transaction code.
df[['Bank', 'Code']]  = df['Transaction Code'].str.split('-', n=1, expand=True)

# Rename the values in the Online or In-person field, Online of the 1 values and In-Person for the 2 values. 
df["Online or In-Person"] = df["Online or In-Person"].replace({1: "Online", 2: "In-Person"})

# Change the date to be the day of the week
df["Transaction Date"] = pd.to_datetime(
  df["Transaction Date"], format="%d/%m/%Y %H:%M:%S"
)

df["Transaction Date"] = df["Transaction Date"].dt.day_name()

# Different levels of detail are required in the outputs. You will need to sum up the values of the transactions in three ways:

groupby_columns = [
  # 1. Total Values of Transactions by each bank
  "Bank", 
  # 2. Total Values by Bank, Day of the Week, and Type of Transaction (Online or In-Person)
  ["Bank", "Online or In-Person" ,"Transaction Date"],
  # 3. Total Values by Bank and Customer Code
  ["Bank", "Customer Code"]
]

# Make list of filenames based on index of groupby_columns
filename = [f"../output/pd-2023-wk1-output-{i + 1}.csv" for i in range(len(groupby_columns))]

def calculate_group_total(groupby_columns, filename):
  (
    df.groupby(groupby_columns)["Value"]
    .sum()
    .sort_values(ascending=False)
    .to_csv(filename)
  )

# Apply calculate_group_total function to each groupby_columns and write csv file
list(
  map(
    calculate_group_total, groupby_columns, filename
  )
)
