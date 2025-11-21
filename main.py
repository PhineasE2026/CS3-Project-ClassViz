import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8-deep')
print(plt.style.available)

# read csv
df = pd.read_csv('class_data_v1.csv')
df = df.head(8)

# Converting columns
df['Birthdate'] = pd.to_datetime(df['Birthdate'])
df['Wakeup Time Weekday'] = pd.to_datetime(df['Wakeup Time Weekday'], format='%H:%M').dt.time
df['Wakeup Time Weekend'] = pd.to_datetime(df['Wakeup Time Weekend'], format='%H:%M').dt.time
df['Vision Impaired'] = pd.to_numeric(df['Vision Impaired']).fillna(0).astype(bool)
df['Night Owl'] = pd.to_numeric(df['Night Owl']).fillna(0).astype(bool)
print(df.info())

# plotting
# plot 1: Hair Length correlation to Height (Inches)
hair_length = df['Hair Length Inches']
height_inches = df['Height Inches']

plt.scatter(hair_length, height_inches, cmap='seismic')
plt.xlabel('Hair Length (Inches)')
plt.ylabel('Height (Inches)')
plt.savefig('hair_to_height.png')
plt.close()

# plot 2: Angel Number to BigFive (A mistake)
big_five_n = df['BigFive Neuroticism']
big_five_e = df['BigFive Extraversion']
big_five_o = df['BigFive Openness']
big_five_c = df['BigFive Conscientious']
big_five_a = df['BigFive Agreeableness']
angel_number = df['Angel Number']

plt.plot(angel_number, big_five_n, c='red')
plt.plot(angel_number, big_five_e, c='blue')
plt.plot(angel_number, big_five_o, c='green')
plt.plot(angel_number, big_five_c, c='pink')
plt.plot(angel_number, big_five_a, c='orange')
plt.xlabel('Angel Number')
plt.ylabel('BigFive Traits')
plt.savefig('angel_number_to_bigfive.png')
plt.close()