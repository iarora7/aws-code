from subapp import app
from flask import Flask, request, jsonify
import psycopg2
import re

# url to use the service
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/searchHouseAvailable?latitude=34.031096&longitude=-118.289951&radius=1.0

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/searchHouseAvailable", methods=['GET'])
def search_house_available():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    radius = (float(request.args.get('radius')) * 1609.34) # user provides the radius in miles which will be converted to meters for the query

    cur = conn.cursor()
    cur.execute("SELECT *  \
                   FROM house_available ha \
                   WHERE ST_DWITHIN( \
                                     ST_GeomFromText('POINT(%s %s)')::geography, \
                                     ST_GeomFromText(ha.location),  \
                                     %s \
                                    )", (latitude, longitude, radius))

    data = cur.fetchall()

    houseList = []
    for row in data:
        latLongList =  re.findall(r"[-+]?\d*\.\d+|\d+", row[11])
        houseDict = {
            'Id'            : row[0],
            'StreetAddress' : row[1].strip(),
            'AptNo'         : row[2],
            'City'          : row[3].strip(),
            'State'         : row[4].strip(),
            'Zip'           : row[5],
            'Spots'         : row[6],
            'Price'         : row[7],
            'StartDate'     : row[8],
            'EndDate'       : row[9],
            'Summary'       : row[10].strip(),
            'Point'         : row[11],
            'Latitude'      : float(latLongList[0]),
            'Longitude'     : float(latLongList[1])

        }
        houseList.append(houseDict)

    return jsonify(houseList = houseList)