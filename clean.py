import pandas as pd
import numpy as np

# we first clean our data
# read data

data = pd.read_csv("austin_weather.csv")

#drop unecessary data
data = data.drop(
    ['Events', 'Date', 'SeaLevelPressureHighInches', 'SeaLevelPressureLowInches']
    , axis=1
)

data = data.replace('T', 0.0)
data = data.replace('-', 0.0)

#save clean data to a csv file
data.to_csv('final_austin.csv')
