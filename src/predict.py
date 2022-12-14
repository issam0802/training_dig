# Libaries needed
import pandas as pd
import pickle


# load data
file_to_open = open('data/models/baummethoden_lr.pickle', 'rb')
trained_model = pickle.load(file_to_open)
file_to_open.close()

prediction_data = pd.read_csv('data/prediction_data.csv', sep=';')
print(trained_model.predict(prediction_data))
