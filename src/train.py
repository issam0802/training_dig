
# Libaries needed
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
import pickle

# Read Data set

data = pd.read_csv('data/auto_mpg.csv', sep=',')
print('Data is: \n', data)
print('Shape is: \n', data.shape)

data = np.random.rand(33, 1)

print('Data is: \n', data)
print('Shape is: \n', data.shape)

#x_input = data.loc[:, data.columns != 'mpg']
#y_output = data['mpg']

# class DataCleaning:


#    def __init__(self, x_input, y_output):
#         self.x_input = x_input
#         self.y_output = y_output


#         return self.x_input, self.y_output

# # def norma


# data_cleaning = DataCleaning()
# print(data_cleaning())
