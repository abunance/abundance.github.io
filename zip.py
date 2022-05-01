# export FLASK_APP=zip.py
import csv
import pandas
import re
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    error = None
    if request.method == "GET":
        return render_template("index.html")
    else: 
        pattern= re.compile("\d{5}")
        input = request.form['zipcode']
        season = request.form.get('season')
        
        if pattern.match(input) and season in ['winter', 'spring', 'summer', 'autumn']: 
            # read in weather data as a dict
            if season == 'winter':
                with open('winter.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
            if season == 'spring':
                if int(input) >= 49650:
                    with open('spring1.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
                else:
                    with open('spring.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
            if season == 'summer':
                if int(input) >= 49650:
                    with open('summer1.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
                else:
                    with open('summer.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
            if season == 'autumn':
                if int(input) >= 49650:
                    with open('autumn1.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
                else:
                    with open('autumn.csv', mode='r') as infile:
                        reader = csv.reader(infile)
                        weatherdata = {rows[0]:[rows[1], rows[2]] for rows in reader}
            
            
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

            #Convert temperature and precp values
            actualtemp = round((y*9/5)+32,1)
            actualwater = round(x*24*7/25.4, 2)

            return render_template("info.html", input=input, season=season, crops=[cropsort.values.tolist()], titles=[''], prep=actualwater, temp=actualtemp)
        else:
            error = "Invalid Zipcode or Season"
            return render_template("index.html", error=error)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/code", methods=["GET"])
def code():
    return render_template("code.html")