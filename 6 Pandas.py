# A series is similar to a 1-D numpy array, contains scalar values of the same type (numeric, character, datetime etc.).
# A dataframe is simply a table where each column is a pandas series. Each row is, by default, assigned an index starting from 0
import numpy as np
import pandas as pd

s = pd.Series([2, 4, 5, 6, 9])
print(s)
print(type(s))

array1 = np.random.randint(1, 9, [4, 5])
print(array1)
# a1 = pd.series(array1.reshape(2,6))
# series1 = pd.Series(array1)
# print(series1)                                    # Data must be 1 Dimensional to convert to Series as series is always 1D

series1 = pd.Series(np.random.randint(1, 7, 7))    # Default data type in int32
print(series1)

date_series = pd.date_range(start="12/20/2020", end="12/31/2020")
print(date_series)
print(type(date_series))

#############################################
# Indexing aand slicing - similar to Numpy arrays

print(array1[1])              # Strictly positional
print(array1[:-2])
print(array1[[1, 3]])           # Strictly positional, indices passed as a list

print(pd.Series([1, 2, 3], index=['a', 'b', 'c']))                  # Explicitly defining index
print(pd.Series(np.array(range(10))**2, index=range(0, 10)))        # Explicitly defining index

#####################################################################################################
# DataFrames

df = pd.DataFrame({'name': ['Vinay', 'Kushal', 'Aman', 'Saif'],
                   'age': [22, 25, 24, 28],
                    'occupation': ['engineer', 'doctor', 'data analyst', 'teacher']})
print(df)
print("\n")

df_read = pd.read_csv(r"C:\Users\vyome\OneDrive\Desktop\PGDMLAI\0 Pre preparatory\Python for Data Science\2_Introduction to "
                      r"Pandas\global_sales_data\cust_dimen.csv")
print(df_read.head(5))              # fetch first 5 rows, if used without argument then fetch all data
print(df_read.tail(5))              # Fetch last five rows
print(df_read.shape)                # Row x Column size
print(df_read.dtypes)               # Data Types for fields
print("\n")
print(df_read.info())               # Need to use parenthesis for this to properly work, gives detailed info on each column
print("\n")
print(df_read.describe())           # Summary of all numeric columns in the dataset
print(df_read.columns)              # column names as the name suggests
print(df_read.values)               # Returns a Numpy array of the dataset
print("\n")

# The default indexing of a dataframe can be changed to a field of choice but with unique values for each row
print(df_read.set_index('Cust_id', drop=False, append=True, inplace=False, verify_integrity=False))
# Only drop default is True, append true appends to existing index, inplace True creates new dataframe and by default is False

"""Sorting can be done in 2 ways namely by Index or by columns"""

print(df_read.sort_index(axis=0, ascending=False))          # Sort rows in descending order by index value
print('\n')
print(df_read.sort_values(by='Customer_Name', axis=0))      # Sort rows by particular column, axis is 0 by default
print('\n')
print(df_read.sort_index(axis=1))                           # Sort columns in ascending order and by default ascending = True

print('\n')
print(df_read.sort_values(by=['Province', 'Customer_Name'], ascending=False))   # Sorting by multiple columns

"""Indexing and Slicing"""
market_df = pd.read_csv(r'C:\Users\vyome\OneDrive\Desktop\PGDMLAI\0 Pre preparatory\Python for Data Science\2_Introduction to '
                        r'Pandas\global_sales_data\market_fact.csv')
print(market_df)
market_df[2:7]
market_df[5::2].head()
print(market_df['Sales'])
print(market_df.Sales)
market_df[['Cust_id', 'Sales', 'Profit']].head()

"""Position(integer: 0 to -1, list or array, slice[1:3], booleans[[True, True, False], [False, True]]) based indexing using "df.iloc" and 
Label based indexing using "df.loc"""
# Position Based Indexing

print(market_df.iloc[2, 4])             # axis 0 = 2nd element and axis 1 = 5th element
print(market_df.iloc[3])                # By default, axis 0 is given 1st position and assigned value 2 and axis 1 all selected
print(market_df.iloc[2, :3])            # 2nd row but only up to 3rd column
print(market_df.iloc[[1, 3, 7], 1:3])   # Pass list of selected/indexed row positions and selected/sliced columns

# Label Based Indexing



