import pandas as pd
l1 = [6,7]
l2 = [4,5]
marks = [l1,l2]
print(marks)

#*****************
import pandas as pd

data = {
    'pranitha': 85,
    'J': 92,
    'Kjc': 88,
    'tp': 95
}

marks_series = pd.Series(data)

print("Marks of Students:")
print(marks_series)
