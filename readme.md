# RAINFALL PREDICTION USING LINEAR REGRESSSION

This is a simple rainfall prediction program that predicts and visualizes the data in a graph to enable observation of different trends.

##DATASET SOURCE

Weather dataset for Austin, Texas obtained from  https://kaggle.com

##The Program

-We first clean our data to get exactly what we want, we drop the unnecessary columns and replace characters since we want to work with numerical values
-After cleaning our data we create a final dataset that we work with in our final prediction

-we read the cleaned data
    -initialize a linear regression classifier
    -train the classifier with our output vector
    -accept a sample data and reshape it
    -predict and output the precipitation from the input
    -visualize the data in a graph of precipitation level against total number of days.

-To further observe various trends in the data input
    -we filter different data parameters to visualize.
    -we then plot the graphs to show the various trends

