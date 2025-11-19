import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-deep')
print(plt.style.available)

# read csv
df = pd.read_csv('class_data_v1.csv')
print(df.info())

# plotting
hairLength = df['Hair Length Inches']
heightInches = df['Height Inches']

plt.scatter(hairLength, heightInches, cmap='seismic')
plt.xlabel('Hair Length (Inches)')
plt.ylabel('Height (Inches)')
plt.savefig('hair_to_height.png')
plt.close()