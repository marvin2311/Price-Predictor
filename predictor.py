#import required modules
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Read CSV-file with iPhone prices
prices = pd.read_csv('iphone_prices.csv', delimiter=';')

#Create scatter plot to visualize iPhonePrices
#plt.scatter(prices['iPhone (Gen.)'], prices['Price (in EUR)'])
#plt.show()

#Create model for predicting prices
model = LinearRegression()

#Train model
model.fit(prices[['iPhone (Gen.)']], prices[['Price (in EUR)']])

#Create dictionary for iPhone prices
predictions = {}

#Loop through each iPhone (13-30) and add the price to the dictionary
for i in range(13,30):
    predictions["iPhone {}".format(i)] = int(model.predict([[i]]))


print(predictions)
