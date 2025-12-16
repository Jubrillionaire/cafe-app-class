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


# Group by (Topic 13, 14)
print("Barista Performance:")
barista_performance = df.groupby('Barista')[['Revenue', 'Quantity']].sum()
print(barista_performance)
print("\n")


# How much did each barista generate for each specific item  (Barista vs item)

print ("Sales Matric (Item vs barista):")
sales_matrix = df.pivot_table(index='Item', columns='Barista', values='Revenue', aggfunc='sum', fill_value=0)
print(sales_matrix)
print("\n")

# Resampling to Daily totals (Topic 10)

daily_revenue = df['Revenue'].resample('D').sum()
print("Daily Revenue:")
print(daily_revenue)


# Get 2-day average
print("2 day average")
print(daily_revenue.rolling(window=2).mean())


print("Day over day growth")
growth = daily_revenue - daily_revenue.shift(1)
print(growth)

