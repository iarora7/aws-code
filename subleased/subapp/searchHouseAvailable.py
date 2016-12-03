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
    cur.execute("SELECT *, ST_AsText(location), ST_Distance(ST_GeomFromText('POINT(%s %s)',4326)::geography, ha.location::geography)/1609.34 as distance  \
                   FROM house_available ha \
                   WHERE ST_DWITHIN( \
                                     ST_GeomFromText('POINT(%s %s)',4326)::geography, \
                                     (ha.location),  \
                                     %s \
                                    )", (longitude, latitude, longitude, latitude, radius))

    data = cur.fetchall()

    houseList = []
    for row in data:
        latLongList =  re.findall(r"[-+]?\d*\.\d+|\d+", row[16])
        houseDict = {
            'id'            : row[0],
            'user_id'       : row[1],
            'StreetAddress' : row[2],
            'AptNo'         : row[3],
            'City'          : row[4].strip(),
            'State'         : row[5].strip(),
            'Zip'           : row[6],
            'Spots'         : row[7],
            'Price'         : row[8],
            'StartDate'     : row[9],
            'EndDate'       : row[10],
            'Title'         : row[11].strip(),
            'Description'   : row[12].strip(),
            'PhoneNumber'   : row[13],
            'Available'     : row[14],
            'Point'         : row[16],
            'Distance'      : row[17],
            'Latitude'      : float(latLongList[1]),
            'Longitude'     : float(latLongList[0])

        }
        houseList.append(houseDict)

    return jsonify(houseList = houseList)

@app.route("/fetchuserhouses", methods=['GET'])
def fetch_user_house():
    userId = long(request.args.get('userId'))
    cur = conn.cursor()
    cur.execute("SELECT * \
                   FROM house_available ha \
                   WHERE user_id=%s", [userId])

    data = cur.fetchall()

    houseList = []
    for row in data:
        houseDict = {
            'id'            : row[0],
            'user_id'       : row[1],
            'StreetAddress' : row[2],
            'AptNo'         : row[3],
            'City'          : row[4].strip(),
            'State'         : row[5].strip(),
            'Zip'           : row[6],
            'Spots'         : row[7],
            'Price'         : row[8],
            'StartDate'     : row[9],
            'EndDate'       : row[10],
            'Title'         : row[11].strip(),
            'Description'   : row[12].strip(),
            'PhoneNumber'   : row[13],
            'Available'     : row[14]
        }
        houseList.append(houseDict)

    return jsonify(houseList = houseList)