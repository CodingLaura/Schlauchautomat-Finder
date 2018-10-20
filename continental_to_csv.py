import csv
import json

import urllib, json
url = "https://contiserver.de/extern/search/public_api/search/json/m/70/latmin/47.3024876979/lngmin/5.98865807458/latmax/54.983104153/lngmax/15.0169958839"
response = urllib.urlopen(url)
data = json.loads(response.read())

f = csv.writer(open("DE_Contintental.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["lat", "lng", "name", "street", "postcode", "city", "phone", "email"])

for x in data["distributors"]:
    f.writerow([x["lat"],
                x["lng"],
                x["name"].encode('utf-8'),
                x["street"].encode('utf-8'),
                x["postcode"].encode('utf-8'),
                x["city"].encode('utf-8'),
                x["phone"].encode('utf-8'),
                x["email"].encode('utf-8')])
