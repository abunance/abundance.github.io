import csv

# read in weather data as a dict
input = '19035'
season = 'spring'
print(type(input))

numer = int(input)
print(type(numer))

if season == 'spring':
    if numer >= 49650:
        with open('spring1.csv', mode='r') as infile:
            reader = csv.reader(infile)
            weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
            print('this one')
    else:
        with open('spring.csv', mode='r') as infile:
            reader = csv.reader(infile)
            weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}

# extract zipcode keys and precp values 
keys = list(weatherdata.keys())

# match inputed zipcode to precp value by indexing both lists
index = keys.index(input) 
print(index)    