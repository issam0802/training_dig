# Libaries needed
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Read Data set

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
