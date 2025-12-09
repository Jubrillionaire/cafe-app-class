import pandas as pd
import numpy as np


data = {
    'OrderID': [101, 102, 103, 104, 105, 106, 102], 
    'Date': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03', '2023-10-03', '2023-10-01'],
    'Item': ['Latte', 'Espresso', 'Latte', 'Muffin', 'Cappuccino', 'Latte', 'Espresso'],
    'Price': [4.50, 3.00, 4.50, np.nan, 4.00, 4.50, 3.00],
    'Qty': [1, 2, 1, 5, 2, 1, 2],
    'Barista': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob']
}


df = pd.DataFrame(data)
print(df)

print("information about dataframe:")
df.info()


# drop duplicate data

df.drop_duplicates(subset=['OrderID'], inplace=True)

mean_price = df['Price'].mean()

df['Price'] =  df['Price'].fillna(value=mean_price)

print("\nDataframe after cleaning:")
print(df)



df.rename(columns={'Qty': 'Quantity'}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df['Revenue'] = df['Price'] * df['Quantity']

print("\nDataframe after transformations:")
            

df.drop(columns=['OrderID'], inplace=True)

print(df)


df.set_index('Date', inplace=True)

print("Orders on Oct 1st, 2023:")
print(df.loc['2023-10-01'])


print("Orders that are bigger than $10 in revenue:")

print(df.query('Revenue > 10'))
