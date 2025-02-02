import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Generating random data
np.random.seed(42)
data = {
    "Study Hours": np.random.randint(1, 10, 50),
    "Marks": np.random.randint(1, 100, 50),
    "Screen Time": np.random.randint(1, 7, 50),
    "Traveling Time": np.random.randint(0, 3, 50),
    "Sleep Hours": np.random.randint(4, 10, 50)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Compute correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()