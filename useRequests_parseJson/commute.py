import requests
import csv
import pandas as pd
import pprint

""" Get all the Google Maps commute times.

* URL Scheme:
    <https://maps.googleapis.com/maps/api/distancematrix/
    json?units=imperial
    &origins=Washington,DC
    &destinations=New+York+City,NY
    &key=YOUR_API_KEY
"""

BASE_URL="https://maps.googleapis.com/maps/api/distancematrix/json"
API_KEY="AIzaSyD6HMXrnAo-gSGtA-jIE-MVWvImVDhJttk"
ADDRESSES="addresses.tsv"

df = pd.read_table(ADDRESSES)

erica_programs_header = "Address-E"
kevin_programs_header = "Address-K"

erica_addresses = list(df[erica_programs_header])
kevin_addresses = list(df[kevin_programs_header])

responses = []

for x, y in zip(erica_addresses, kevin_addresses):
    payload = {
            "units": "imperial",
            "origins": x,
            "destinations": y,
            "mode": "driving",
            "key": API_KEY
            }
    r = requests.get(BASE_URL, params=payload)
    responses.append(r.json())

for r in responses:
    with open("distances.txt", "a") as f:
        f.write("{}\t{}\t{}\n".format(
            r['destination_addresses'][0], 
            r['origin_addresses'][0], 
            r['rows'][0]['elements'][0]['duration']['text']
            ))

