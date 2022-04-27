zipcode = '00601'

import csv

with open('weather.csv', mode='r') as infile:
    reader = csv.reader(infile)
    weatherdata = {rows[0]:rows[3] for rows in reader}
keys = list(weatherdata.keys())
values = list(weatherdata.values())

index = keys.index(zipcode)
x = values[index]
# FEED SPECIFIC TEMPERATURE AND WATER
