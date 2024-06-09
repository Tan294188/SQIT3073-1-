import pandas as pd
df=pd.read_csv("ipi.csv")
df2=pd.DataFrame(df[20,3])
print(df2)
import matplotlib.pyplot as plt
import numpy as np
# Generate random data
num_points = 50
x = np.random.uniform(0, 10, num_points)
y = np.random.uniform(0, 10, num_points)
colors = np.random.uniform(0, 5, num_points)
# Create the plot
plt.scatter(x, y, s=100, c=colors, marker='o')
# Show the plot
plt.show()
