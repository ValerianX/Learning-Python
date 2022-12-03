# A series is similar to a 1-D numpy array, contains scalar values of the same type (numeric, character, datetime etc.).
# A dataframe is simply a table where each column is a pandas series.
import numpy as np
import pandas as pd

s = pd.Series([2, 4, 5, 6, 9])
print(s)
print(type(s))

array1 = np.random.randint(1, 9, [4, 5])
# a1 = pd.series(array1.reshape(2,6))
# series1 = pd.Series(array1)
# print(series1)                                    # Data must be 1 Dimensional to convert to Series as series is always 1D

series1 = pd.Series(np.random.randint(1, 7, 7))    # Default data type in int32
print(series1)

date_series = pd.date_range(start="12/20/2020", end="12/31/2020")
print(date_series)
print(type(date_series))

#############################################





