<<<<<<< HEAD
=======

>>>>>>> 39e306e8810c31a0045188d4043e45b4a64d3eed
# Libaries needed
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
<<<<<<< HEAD
=======
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
>>>>>>> 39e306e8810c31a0045188d4043e45b4a64d3eed
import pickle

# Read Data set

<<<<<<< HEAD
data = pd.read_csv('data/auto_mpg.csv', sep=';')

# show data details
print('data = \n', data.head())
print('**************************************')
print('data.describe = \n', data.describe())
print('**************************************')

data = data.sample(frac=1)
x_inputs = data.drop('mpg', axis=1)
y_output = data['mpg']

# creat model

x_train, x_test, y_train, y_test = train_test_split(
    x_inputs, y_output, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

con = pd.DataFrame(model.coef_, x_inputs.columns, columns=['Con'])

y_pred = model.predict(x_test)

filename = 'data/models/baummethoden_lr.pickle'
pickle.dump(model, open(filename, 'wb'))
=======
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
>>>>>>> 39e306e8810c31a0045188d4043e45b4a64d3eed
