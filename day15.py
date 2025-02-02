import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data = {
    "customer_id":[1, 2, 3, 4],
    "gender": ["male", "female", "male", "female"],
    "city": ["Hyderabad", "pune", "Banglore", "Mumbai"],
    "fruits":["Mango", "Orange", "Apple", "Banana"]
}
df = pd.DataFrame(data)
print("Original Data: ")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city", "fruits"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)


#******************************************

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
data = {
    "customer_id":[1, 2, 3, 4],
    "gender": ["male", "female", "male", "female"],
    "city": ["Hyderabad", "pune", "Banglore", "Mumbai"],
    "fruits":["Mango", "Orange", "Apple", "Banana"]
}
df = pd.DataFrame(data)
print("Original Data: ")
print(df)
one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city", "fruits"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])
encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
df = pd.concat([df.drop(columns_to_encode, axis=1), encoded_df], axis=1)
print("\nEncoded Data: ")
print(df)


#*************************************


#Label Encoder 

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data ={
    "Customer_id":[1,2,3,4,],
    "Ranks":["First","Second","Third","Fourth"],
    "frutis":["apple","bananna","orange","kivi"],
    "Gender":["Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
print(f"The Data is :\n\n {df}\n")
label_encoder = LabelEncoder()
df["encoded_ranks"] = label_encoder.fit_transform(df["Ranks"])
df["encoded_frutis"] = label_encoder.fit_transform(df["frutis"])
print(f"The LabeleEncoded Data id :\n \n{df}\n")