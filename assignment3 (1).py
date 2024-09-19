# -*- coding: utf-8 -*-
"""Assignment3.ipynb
"""

df = pd.read_csv("netflix2.csv")
df

df.shape

df.info()

df.describe()

null_values = df.isnull().sum()
null_values

duplicate_samples = df[df.duplicated(keep=False)]
print(duplicate_samples)

df_new = df.drop(columns="show_id", inplace=False)
df.head()

# prompt: get duplicate samples from df

duplicate_samples = df_new[df_new.duplicated(keep=False)]
print(duplicate_samples)

# prompt: drop duplicated samples

df_new.drop_duplicates(inplace=True)

df_new.shape

df_new.columns

df_new.rename(columns={
    'type': 'Type',
    'title': 'Title',
    'director': 'Director',
    'country': 'Country',
    'date_added': 'Date',
    'release_year': 'ReleaseYear',
    'rating': 'Rating',
    'duration': 'Duration',
    'listed_in': 'ListedIn'
}, inplace=True)
df_new.head()

type_counts = df_new['Type'].value_counts()
type_counts

import matplotlib.pyplot as plt
plt.figure(figsize=(3,3))
mylabels = ['Movie','TVshow']
myexplode = [0, 0.1]
colors = ['lightcoral', 'lightskyblue']
plt.pie(type_counts,labels = mylabels, explode = myexplode, shadow = True, autopct="%1.3f%%", colors=colors)
plt.title("Netflix Content Types")
plt.show()

type_counts = df_new['Director'].value_counts()
type_counts

import matplotlib.pyplot as plt
import numpy as np
director_counts = top_directors_df['Director'].value_counts()
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(director_counts)))
plt.bar(director_counts.index, director_counts.values, color=colors)

plt.xlabel('Director')
plt.ylabel('Number of Titles')
plt.title('Top Directors on Netflix')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

country_counts = df['Country'].value_counts()
country_df = pd.DataFrame({
    'Country': country_counts.index,
    'Count': country_counts.values
})

top_countries_df = country_df.nlargest(50, 'Count')
top_countries_df

top_countries_df = top_countries_df[top_countries_df['Country'] != 'Not Given']
top_countries_df

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.plot(top_countries_df['Country'], top_countries_df['Count'], linestyle='dotted', marker='o', color='g')
plt.xticks(rotation=90)
plt.title('Top 50 Countries by Count')
plt.xlabel('Country')
plt.ylabel('Count')
plt.tight_layout()
plt.show()