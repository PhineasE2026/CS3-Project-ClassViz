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

# plot 3: Java Rating to Caffeine Drinks Per Week
java_rating = df['Java Rating']
caffeine_per_week = df['Caffeine Drinks Per Week']

plt.scatter(java_rating, caffeine_per_week)
plt.xlabel('Java Rating')
plt.ylabel('Caffeine Drinks Per Week')
plt.savefig('java_rating_to_caffeine_per_week.png')
plt.close()

# plot 4: 13 Year Club to Instagram Followers
thirteen_year_club = df['13 Year Club']
instagram_followers = df['Instagram Followers']

plt.bar(thirteen_year_club, instagram_followers)
plt.xlabel('13 Year Club')
plt.ylabel('Instagram Followers')
plt.savefig('13_year_club_to_instagram_followers.png')
plt.close()

# plot 5: Hogwarts House to Temperature Preference
hogwarts_house = df['Hogwarts House']
temp_preference = df['Temperature Preference']

plt.plot(hogwarts_house, temp_preference)
plt.xlabel('Hogwarts House')
plt.ylabel('Temperature Preference')
plt.savefig('hogwarts_house_to_temp_preference.png')
plt.close()

# plot 6: College Major to Favorite Subject
college_major = df['College Major']
favorite_subject = df['Favorite Subject']

plt.plot(college_major, favorite_subject)
plt.xlabel('College Major')
plt.ylabel('Favorite Subject')
plt.savefig('college_major_to_favorite_subject.png')
plt.close()

# plot 7: Jewish to Years at BWL
jewish = df['Jewish']
years_at_bwl = df['Years at BWL']

plt.bar(jewish, years_at_bwl)
plt.xlabel('Jewish')
plt.ylabel('Years at BWL')
plt.savefig('jewish_to_years_at_bwl.png')
plt.close()

# plot 8: Vision Impaired to Extraversion
vision_impaired = df['Vision Impaired']

plt.bar(vision_impaired, big_five_e)
plt.xlabel('Vision Impaired')
plt.ylabel('BigFive Extraversion')
plt.savefig('vision_impaired_to_bigfive_extraversion')
plt.close()

# plot 9: Hair Color to Song Genre
hair_color = df['Hair Color']
song_genre = df['Song Genre']

plt.plot(hair_color, song_genre)
plt.xlabel('Hair Color')
plt.ylabel('Song Genre')
plt.savefig('hair_color_to_song_genre.png')
plt.close()

# plot 10: Current Obsession to Favorite Show
current_obsession = df['Current Obsession']
favorite_show = df['Favorite Show']

plt.plot(current_obsession, favorite_show)
plt.xlabel('Current Obsession')
plt.ylabel('Favorite Show')
plt.savefig('current_obsession_to_favorite_show.png')
plt.close()