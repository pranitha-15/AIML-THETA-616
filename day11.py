import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    'square_feet_area': [8500, 8000, np.nan, 9000, 5000, 7500, 6000, 7000, 10000, 4000],
    'Year_built': [2004, 2006, 2009, 2002, np.nan, 2000, 2001, 2003, np.nan, 2007],
    'over_all_condition': [5, 4, 6, 7, np.nan, 8, 6, np.nan, 7, 4],
    'ready_to_move': ['yes', 'yes', 'yes', np.nan, 'no', 'yes', 'yes', 'yes', np.nan, 'yes'],
    'Sale_price': [200000, 180000, 190000, 160000, 150000, 185000, 175000, 170000, 195000, 165000]
}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

df['square_feet_area'].fillna(df['square_feet_area'].mean(), inplace=True)
df['Year_built'].fillna(df['Year_built'].mean(), inplace=True)
df['over_all_condition'].fillna(df['over_all_condition'].mean(), inplace=True)


df['ready_to_move'].fillna(df['ready_to_move'].mode()[0], inplace=True)  


print("\nDataFrame after filling missing values with mean (for numeric)")
print(df)