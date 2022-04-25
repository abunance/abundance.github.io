# export FLASK_APP=zip.py
import pgeocode
import numpy
import pandas
import re
from flask import Flask, render_template, request
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
            # FEED SPECIFIC TEMPERATURE AND WATER
            x= .1
            y = 15

            # converting csv to html
            collist = ['CROP','WATERmm','TEMPC','WATER','TEMP']
            croptable = pandas.read_csv('crops.csv', usecols=collist)
            weighted=[]
            for index, row in croptable.iterrows():
                T = row['TEMPC']
                W = row['WATERmm']
                weighted.append(abs(x-W)*.4/x+abs(y-T)*.6/y)

            croptable['similarity'] = weighted
            cropsort = croptable.sort_values(by=['similarity'])
    
            return render_template("info.html", input=input, season=season, crops=[cropsort.values.tolist()], titles=[''])
        else:
            error = "Invalid Zipcode or Season"
            return render_template("index.html", error=error)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")