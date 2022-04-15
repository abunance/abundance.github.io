import pgeocode
import numpy
import pandas
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/info', methods=['POST'])
def zipcode():
    input = request.form['zipcode']
    # country is always us
    country = pgeocode.Nominatim('us')
        
    # input zipcode --> make dynamic
    zipcode = country.query_postal_code(input)

    lat = zipcode["latitude"]
    lon = zipcode["longitude"]
    return render_template("info.html", lat=lat, lon=lon)