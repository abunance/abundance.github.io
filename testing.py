input = '00601'

import csv
import pandas

# read in weather data as a dict
with open('summer.csv', mode='r') as infile:
    reader = csv.reader(infile)
    weatherdata = {rows[0]:[rows[3], rows[5]] for rows in reader}

# extract zipcode keys and precp values 
keys = list(weatherdata.keys())
values = list(weatherdata.values())

# match inputed zipcode to precp value by indexing both lists
index = keys.index(input)

# FEED SPECIFIC TEMPERATURE AND WATER
x = values[index][0]
y = values[index][1]

#must convert x string to float for calculations
x = float(x)
y = float(y)

# converting csv to html
croplist = ['CROP','WATERmm','TEMPC','WATER','TEMP']
croptable = pandas.read_csv('crops.csv', usecols=croplist)
weighted=[]

# extract temp and water for each crop
for index, row in croptable.iterrows():
    T = row['TEMPC']
    W = row['WATERmm']
    # created weighted similarity to region's temp and water
    weighted.append(abs(x-W)*.4/x+abs(y-T)*.6/y)
croptable['similarity'] = weighted

# sort crops by similarity
cropsort = croptable.sort_values(by=['similarity'])
