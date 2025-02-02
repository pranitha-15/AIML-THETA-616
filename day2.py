import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Marks': [85, 78, 92, 88, 95]
}

df = pd.DataFrame(data)

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(assign_grade)

print("Student Grades:\n")
print(df)

#**********************************


import pandas as pd
screen_time = [2,3,4,7]
sleep_hours = [4,7,10,11]
stu_name = ["veerachary","renuka","pranitha","arun"]
dict1 = {
  "screen_time":screen_time,
  "sleep_hours":sleep_hours,
  "stu_name":stu_name
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)
