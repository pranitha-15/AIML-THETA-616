import numpy as np

arr = np.array([[[1, 2, 3], [4,5,6]], [[7, 8, 9],[10, 11, 12]]])

print(arr)
print(arr[1, 1, 2])
"******************************************************"
import numpy as np

arr = np.array([[[1, 2, 3], [4,5,6]], [[7, 8, 9],[10, 11, 12]]])

print(arr[1:5:2])

"*******************************************"

import pandas as pd

patient_info = pd.DataFrame({
    'patient Name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'Age': [5, 10, 3],
    'Date of appointment': ['2023-10-01', '2023-10-02', '2023-10-03'],
    'Patient id': [1, 2, 3]
})


drag_quantity = pd.DataFrame({
    'drag name': ['Drug A', 'Drug B', 'Drug C'],
    'quantity': [10, 20, 30],
    'patient_id': [1, 2, 3]
})


filtered_patient_info = patient_info[patient_info['Age'] < 6][['patient Name', 'Age']]


merged_df = pd.merge(patient_info, drag_quantity, left_on='Patient id', right_on='patient_id', how='inner')

print("Filtered Patient Information:")
print(filtered_patient_info)
print("\nMerged Dataframe:")
print(merged_df)