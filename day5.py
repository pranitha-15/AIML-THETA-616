import pandas as pd
screen_time = [2,3,4,7]
sleep_hours = [4,7,10,11]
stu_name = ["pranitha","Jc","gayatri","Bhavya"]
dict1 = {
  "screen_time":screen_time,
  "sleep_hours":sleep_hours,
  "stu_name":stu_name
}

df = pd.DataFrame(dict1)
print(df)

#********************************
# Importing the required library
import pandas as pd

# Creating dict1 and dict2
dict1 = { 'Customer_id': [1, 2, 3, 4, 5, 6], 'Product': ['Television', 'er', 'evision', 'Televi', 'Tesion', 'Teln']}
dict2 = {'Customer_id': [2, 4, 6, 8], 'State': ['California', 'California', 'Texas', 'Texas']}

# Converting dicts to DataFrames
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

# Displaying the DataFrames
print("DataFrame 1 (df1):")
print(df1)

print("\nDataFrame 2 (df2):")
print(df2)

# Performing inner join
inner_join = pd.merge(df1, df2, on='Customer_id', how='inner')

# Performing outer join
outer_join = pd.merge(df1, df2, on='Customer_id', how='outer')

# Displaying the results
print("\nInner Join:")
print(inner_join)

print("\nOuter Join:")
print(outer_join)
