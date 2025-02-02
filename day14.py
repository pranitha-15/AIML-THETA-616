import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#sample dataset with multiple features

data={
    "age":[25,30,35,40,45],
    "height":[150,160,170,180,190],
    "weight":[50,60,70,80,90]
}


df=pd.DataFrame(data)
print("Original Dataframe")

print(df)

scaler=MinMaxScaler()

#normalize the dataset

normalized_data=scaler.fit_transform(df)

# create a new dataframe with normalized data
normalized_df=pd.DataFrame(normalized_data,columns=df.columns)
print("\nNormalized Dataframe (scaled to range [0, 1]):")
print(normalized_df)


#***************************

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = {
    "age": [25, 30, 35, 40, 45],
    "height": [150, 170, 180, 160, 200],
    "weight": [60, 70, 80, 75, 90]
}
df = pd.DataFrame(data)
print("Original Data: ")
print(df)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print("\nNormalized Data (scaled to range [0, 1]): ")
print(normalized_df)
standardized_data = (df - df.mean()) / df.std()
standardized_df = pd.DataFrame(standardized_data, columns=df.columns)
print("\nStandardized Data (mean = 0, std = 1): ")
print(standardized_df)