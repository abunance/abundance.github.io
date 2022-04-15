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
        if pattern.match(input):
            data = []
            # country is always us
            country = pgeocode.Nominatim('us')
             
            zipcode = country.query_postal_code(input)
            data.append(zipcode["latitude"])
            data.append(zipcode["longitude"])
            return render_template("info.html", data=data)
        else:
            error = "Invalid Zipcode"
            return render_template("index.html", error=error)
