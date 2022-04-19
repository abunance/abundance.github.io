# export FLASK_APP=zip.py
import pgeocode
import numpy
import pandas
import re
from flask import Flask, render_template, request
app = Flask(__name__)

df = pandas.read_csv('crops.csv')
df.to_csv('crops.csv', index=None)

@app.route("/", methods=["POST", "GET"])
def index():
    error = None
    if request.method == "GET":
        return render_template("index.html")
    else: 
        pattern= re.compile("\d{5}")
        input = request.form['zipcode']
        if pattern.match(input):
            data = []
            # country is always us
            country = pgeocode.Nominatim('us')
             
            season = request.form.get('season')
            zipcode = country.query_postal_code(input)
            data.append(zipcode["latitude"])
            data.append(zipcode["longitude"])
            
            # converting csv to html
            croptable = pandas.read_csv('crops.csv')
            cropdata = croptable['CROP']
            return render_template("info.html", data=data, input=input, season=season, crops=cropdata)
        else:
            error = "Invalid Zipcode"
            return render_template("index.html", error=error)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
