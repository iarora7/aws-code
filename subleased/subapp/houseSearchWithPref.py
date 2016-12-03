from subapp import app
from flask import Flask, request, jsonify
import psycopg2
import re
import math

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

# lat1 = 34.029367
# lon1 = -118.287419
#
# lat2 = 34.031053
# lon2 = -118.288293

cur = conn.cursor()

# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/houseSearchWithPref?latitude=34.031096&longitude=-118.289951&radius=2&gym=true&hospital=true&school=false&grocery=false
@app.route("/houseSearchWithPref", methods=['GET'])
def house_search_with_pref():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    gym = (request.args.get('gym'))
    hospital = (request.args.get('hospital'))
    school = (request.args.get('school'))
    grocery = (request.args.get('grocery'))
    radius = (float(request.args.get('radius')) * 1609.34)

    cur.execute("SELECT *, ST_AsText(location), ST_Distance(ST_GeomFromText('POINT(%s %s)',4326)::geography, ha.location::geography)/1609.34 as distance  \
                       FROM house_available ha \
                       WHERE ST_DWITHIN( \
                                         ST_GeomFromText('POINT(%s %s)',4326)::geography, \
                                         (ha.location),  \
                                         %s \
                                        )", (longitude, latitude, longitude, latitude, radius))
    data = cur.fetchall()
    houselist = []
    for row in data:
        latLongList = re.findall(r"[-+]?\d*\.\d+|\d+", row[16])
        houseDict = {
            'id': row[0],
            'user_id': row[1],
            'StreetAddress': row[2],
            'AptNo': row[3],
            'City': row[4].strip(),
            'State': row[5].strip(),
            'Zip': row[6],
            'Spots': row[7],
            'Price': row[8],
            'StartDate': row[9],
            'EndDate': row[10],
            'Title': row[11].strip(),
            'Description': row[12].strip(),
            'PhoneNumber': row[13],
            'Available': row[14],
            'Point': row[16],
            'Distance': row[17],
            'Latitude': float(latLongList[1]),
            'Longitude': float(latLongList[0])

        }
        houselist.append(houseDict)

    s = ""
    gymlist=[]
    hospitallist=[]
    schoollist=[]
    grocerylist=[]

    if gym == "true":
        s += "Gym, "
        gymlist = getListofPublicPlaces("Gym")
    if hospital == "true":
        s += "hopsital, "
        hospitallist = getListofPublicPlaces("Hospital")
    if school == "true":
        s += "school, "
        schoollist = getListofPublicPlaces("School")
    if grocery == "true":
        s += "grocery"
        grocerylist = getListofPublicPlaces("Grocery Store")

    if(len(gymlist) > 0 and len(houselist) > 0):
        print("refine on gyms")
        houselist = refineResult(gymlist, houselist)

    if(len(hospitallist) > 0 and len(houselist) > 0):
        print("refine on hospital")
        houselist = refineResult(hospitallist, houselist)

    if(len(schoollist) > 0 and len(houselist) > 0):
        print("refine on school")
        houselist = refineResult(schoollist, houselist)

    if(len(grocerylist) > 0 and len(houselist) > 0):
        print("refine on grocery")
        houselist = refineResult(grocerylist, houselist)

    return jsonify(houseList = houselist)

def refineResult(placelist, houselist):
    refined_result=[]
    for place in placelist:
        for house in houselist:
            lat1, lon1, lat2, lon2 = getLatLng(place, house)
            miles = calculateDistance(lat1, lon1, lat2, lon2)
            if miles <= 1.0:
                refined_result.append(house)
    refined_result = list({v['id']: v for v in refined_result}.values())
    print("len of place list:", len(placelist))
    print("len of house list before refine:", len(houselist))
    houselist = refined_result
    print("len of house list after refine:", len(houselist))
    return houselist


def getLatLng(place, house):
    lat1 = float(place['latitude'])
    lon1 = float(place['longitude'])
    lat2 = float(house['Latitude'])
    lon2 = float(house['Longitude'])
    return lat1, lon1, lat2, lon2

def getListofPublicPlaces(public_place):
    print(public_place)
    cur.execute("Select *, ST_AsText(location)  \
                from public_places p, category c \
                where p.category_id = c.id \
                and c.category_type = %s", (public_place,))
    data = cur.fetchall()
    public_places = []
    for row in data:
        latLongList = re.findall(r"[-+]?\d*\.\d+|\d+", row[11])
        place = {
            'id': row[0],
            'category_id': row[1],
            'name': row[2].strip(),
            'st_address': row[4],
            'city': row[5],
            'state': row[6],
            'zip': row[7],
            'rating': row[8],
            'category_type': row[10],
            'location': row[11],
            'latitude': latLongList[1],
            'longitude': latLongList[0]
        }
        public_places.append(place)
    return public_places

def calculateDistance(lat1, lon1, lat2, lon2):
    polar_radius = 6356750
    equatorial_radius = 6378200
    # Latitude Difference [m] =|Lat1 - Lat2| *(pi / 180) * polar radius
    # Longitude Difference [m] = |Lon1 - Lon2|*(pi / 180 )* (equatorial radius * cosine( (Lat1 + Lat2) / 2 )
    # Distance = sqrt( latitude diference^2 + longitude difference^2 )
    lat_diff = math.fabs(lat1 - lat2) * (3.14/180) * polar_radius
    lon_diff = math.fabs(lon1 - lon2) * (3.14/180) * (equatorial_radius * math.cos((lat1 + lat2) / 2))
    distance = math.sqrt(math.pow(lat_diff,2) + math.pow(lon_diff,2))
    return distance/1609.34

# miles = calculateDistance(lat1, lon1, lat2, lon2)
# print("miles : ", miles)