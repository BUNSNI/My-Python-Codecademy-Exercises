#Import all the necessary libraries

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Make a get request of the website
webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

#Use BeautifulSoup to parse the data into a readable format
soup = BeautifulSoup(webpage.content, 'html.parser')

#Use find_all() to search for class attributes called Rating and save to a variable list_ratings
list_ratings = soup.find_all(attrs={'class' : 'Rating'})
ratings = []

#Loop through list_ratings and append all numbers to an empty list
for x in list_ratings:
  number = x.text
  try:
    float(number)
    ratings.append(float(number))
  except ValueError:
    pass

#Use matplotlib to display data
plt.hist(ratings)
plt.show()

#Access all company names, saving them to an empty list
company_names = []
names = soup.find_all(attrs = {'class' : 'Company'})
for name in names:
  text = name.text
  company_names.append(text)
del company_names[0]


cocoa_list = []
cocoa = soup.select('.CocoaPercent')
#print(cocoa)

for percent in cocoa:
  just_text = percent.text
  cocoa_perc = just_text.strip('%')
  try:
    cocoa_list.append(int(float(cocoa_perc)))
  except ValueError:
    pass

#Create a dataframe using panda, identifying column name keys and values
df = pd.DataFrame({'Company': company_names, 'Ratings': ratings, 'CocoaPercentage': cocoa_list})
#Group the dataframe by Company name and get the mean values for each company
gk = df.groupby('Company').Ratings.mean()
#Select the companies with the 10 highest ratings
best_ratings = gk.nlargest(10)
#print(best_ratings)

plt.clf()

#Create a scatter plot using dataframes from cocoapercentage and ratings
plt.scatter(df.CocoaPercentage, df.Ratings)

#Create a line of best fit for the scatter plot
z = np.polyfit(df.CocoaPercentage, df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

#Display the plot
plt.show()
