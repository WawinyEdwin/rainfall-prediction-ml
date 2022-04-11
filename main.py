from turtle import color
import pandas as pd
import numpy as np

import sklearn as sk
from sklearn.linear_model  import LinearRegression

import matplotlib.pyplot as plt


# read cleaned data 
data = pd.read_csv("final_austin.csv")

# drop last column 
X = data.drop(["PrecipitationSumInches"], axis=1)

#output label
Y = data['PrecipitationSumInches']

# reshape into a 2d vector
Y = Y.values.reshape(-1, 1)

# plot a graph to observe
day_index = 798
days = [i for i in range(Y.size)]

# init a linear classifier
clf = LinearRegression()

# train classifier with the output vector
clf.fit(X, Y)

#sample data input
inp = np.array([ [74], [60], [45], [67] , [49], [43], [33], [45],
[57], [29.68], [10], [7], [2], [0], [20], [4], [31]]
)

# reshape input 
inp = inp.reshape(1, -1)

# print output 
print("The Precipitation in inches for the input is: ", clf.predict(inp))

print("The precipitation trend graph is : ")

#visualize data in a graph

# graph of precipitation level over total number days 
plt.scatter(days, Y, color='g')
plt.scatter(days[day_index], Y[day_index], color='r')
plt.title('Precipitation Level')
plt.xlabel('Days') #horizontal axis
plt.ylabel('Precipitation In Inches') #vertical axis

plt.show()

#graph to observe the trends, against precipitation level.
x_f = X.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 'SeaLevelPressureAvgInches', 'VisibilityAvgMiles', 'WindAvgMPH'], axis=1)

print("Precipitation vs selected attr Graph: ")

for i in range(x_f.columns.size):
    plt.subplot(3, 2, i + 1)
    plt.scatter(days, x_f[x_f.columns.values[i] [: 100]], color='g')
    plt.scatter(days[day_index], x_f[x_f.columns.values[i]] [day_index], color='r')
    plt.title(x_f.columns.values[i])

plt.show()




