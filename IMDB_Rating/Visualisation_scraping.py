import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df5=pd.read_csv('Akshay_IMDb_Scraping.csv')
# print(f.shape)
df5.columns=df5.columns.str.replace('Unnamed: 0','Sr.No')
# print(df5.head())
# print(df5.columns)

# print(df5.info()) # 3 Data types

# print(df5.describe())

# print(df5.isnull().sum()) #NO NUll Values

# print(df5['Rating'].value_counts())


''' Bar Graph of Rating values vs Count of Rating'''
plt.figure(figsize=(20,20))
ax=sb.countplot(data=df5 , x='Year')
plt.ylabel('freq')
plt.xticks(rotation=90)
plt.xlabel('Ratings')
plt.title('freq of each Rating')

for p in ax.patches:
    ax.annotate(p.get_height(),(p.get_x()+0.15,p.get_height()+1))

plt.savefig('Rating_bar_graph.svg')
plt.show()

'''Bar Graph for all Colums'''
# plt.figure(figsize=(10,10))
# ax=sb.pairplot(df5)
# plt.show()

'''Scattering of Year vs Rating'''
# plt.scatter(data=df5,x='Year',y='Rating')
# plt.xlabel('Year')
# plt.ylabel('Rating')
# plt.show()

'''jointplot of Rating vs Year'''
# plt.figure(figsize=(10,7))
# sb.jointplot(data=df5,x='Year',y='Rating',kind='hist')
# plt.show()


'''Heat Maps Year vs Rating'''
# plt.hist2d(data=df5,x='Year',y='Sr.No',cmin=0.5)
# plt.colorbar()
# plt.xlabel("Year")
# plt.ylabel("Rating")
# plt.show()
