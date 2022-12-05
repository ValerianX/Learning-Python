# A series is similar to a 1-D numpy array, contains scalar values of the same type (numeric, character, datetime etc.).
# A dataframe is simply a table where each column is a pandas series.
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

# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# retrieving rows by loc method
row1 = data.loc[3]

# retrieving rows by iloc method
row2 = data.iloc[3]

# checking if values are equal
row1 == row2





