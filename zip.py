import pgeocode
import numpy
import pandas

input = 19035
# country is always us
country = pgeocode.Nominatim('us')

# input zipcode --> make dynamic
zipcode = country.query_postal_code(input)

lat = zipcode["latitude"]
lon = zipcode["longitude"]

print(lat)
print(lon)

FLASK?