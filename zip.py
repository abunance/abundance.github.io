import pgeocode
import numpy
import pandas
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else: 
        return render_template("info.html")

#@app.route('/info', methods=['POST'])
#def info():
    #data = []
    #input = request.form['zipcode']
    # country is always us
    #country = pgeocode.Nominatim('us')
        
    # input zipcode --> make dynamic
    #zipcode = country.query_postal_code(input)
    #data.append(zipcode["latitude"])
    #data.append(zipcode["longitude"])
    