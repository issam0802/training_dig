import requests
import pandas as pd
import numpy as np
import datetime
import re
import bs4
import json
import matplotlib.pyplot as plt

#{temperature: -2.6, windspeed: 6.9, winddirection: 43, weathercode: 3, time: "2022-12-15T12:00"}
# aktuelle_wetter = my_city[{'current_weather': ['temperature', 'windspeed',
#                           'winddirection', 'weathercode', 'time']}]


headers = {'Content-Type': 'application/json'}
base_url = 'https://api.open-meteo.com/v1/dwd-icon?latitude=50.12&longitude=8.83&hourly=temperature_2m&current_weather=true&timezone=Europe%2FBerlin&start_date={}&end_date={}'
start_date = datetime.date.today()
#date_exp = r'\d{2}-\d{2}-\d{4}'
end_date = start_date + datetime.timedelta(days=5)
res = requests.get(base_url.format(start_date, end_date), headers=headers)
my_city = res.json()
# print(my_city)
breitenband = my_city['latitude']
langenband = my_city['longitude']
wetter_aktuell = my_city['current_weather']
akt_temp = wetter_aktuell['temperature']

print(
    f'Latitude-Offenbach: {breitenband} und Longitude-Offenbach: {langenband}')
print(f'Das akteulle Wetter in Offenbach am Main: {akt_temp}')

wetter_vorhersage = my_city['hourly']
key_list = wetter_vorhersage['time']
value_list = wetter_vorhersage['temperature_2m']
dreitage_vorhersage = dict(zip(key_list, value_list)).items()

df = pd.DataFrame(dreitage_vorhersage, columns=[
                  'Temperatur Tag/Std', 'Grad in C'])
#ser = pd.Series(dreitage_vorhersage)
print(f'Die Drei Tage Wetter Vorhersage: \n {df.transpose()}')

# temp_akt_tag = df['Grad in C'][0:24]
# print(temp_akt_tag)


file_name = './src/wetter_off.json'
json.dump(my_city, open(file_name, 'w'))

# plt.plot(key_list, value_list, 'r')
# plt.xlabel('Temperatur Tag/Std')
# plt.ylabel('Grad in C')
# plt.title('Offenbach wetter')
# plt.show()
