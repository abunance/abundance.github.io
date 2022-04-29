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
        input = str(request.form['zipcode'])
        season = request.form.get('season')
        
        if pattern.match(input) and season in ['winter', 'spring', 'summer', 'autumn']: 
            # read in weather data as a dict
            if season == 'winter':
                with open('winter.csv', mode='r') as infile:
                    reader = csv.reader(infile)
                    weatherdata = {rows[0]:rows[3] for rows in reader}
            if season == 'spring':
                with open('spring.csv', mode='r') as infile:
                    reader = csv.reader(infile)
                    weatherdata = {rows[0]:rows[3] for rows in reader}
            if season == 'summer':
                with open('summer.csv', mode='r') as infile:
                    reader = csv.reader(infile)
                    weatherdata = {rows[0]:rows[3] for rows in reader}
            if season == 'autumn':
                with open('autumn.csv', mode='r') as infile:
                    reader = csv.reader(infile)
                    weatherdata = {rows[0]:rows[3] for rows in reader}

            # extract zipcode keys and precp values 
            keys = list(weatherdata.keys())
            values = list(weatherdata.values())

            # match inputed zipcode to precp value by indexing both lists
            index = keys.index(input)

            # FEED SPECIFIC TEMPERATURE AND WATER
            x = values[index]
            y = 15
            #must convert x string to float for calculations
            z = float(x)

            # converting csv to html
            croplist = ['CROP','WATERmm','TEMPC','WATER','TEMP']
            croptable = pandas.read_csv('crops.csv', usecols=croplist)
            weighted=[]

            # extract temp and water for each crop
            for index, row in croptable.iterrows():
                T = row['TEMPC']
                W = row['WATERmm']
                # created weighted similarity to region's temp and water
                weighted.append(abs(z-W)*.4/z+abs(y-T)*.6/y)
            croptable['similarity'] = weighted

            # sort crops by similarity
            cropsort = croptable.sort_values(by=['similarity'])

            #Convert temperature and precp values
            actualtemp = (y*9/5)+32
            actualwater = z*24*7/25.4

            return render_template("info.html", input=input, season=season, crops=[cropsort.values.tolist()], titles=[''], prep=actualwater, temp=actualtemp)
        else:
            error = "Invalid Zipcode or Season"
            return render_template("index.html", error=error)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")