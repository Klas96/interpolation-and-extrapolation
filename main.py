import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from datetime import datetime



#Creating a Series by passing a list of values, letting pandas create a default integer index:

s = pd.Series([1, 3, 5, np.nan, 6, 8])

#Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:

dates = pd.date_range('20130101', periods=6)

#Creating a DataFrame by passing a dict of objects that can be converted to series-like.

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})


#The columns of the resulting DataFrame have different dtypes.


#pd.read_csv()

#print(s)
#print(dates)
#print(df2.dtypes)
#print(df2.A)

s.plot(figsize=(18,5))

plt.show()
