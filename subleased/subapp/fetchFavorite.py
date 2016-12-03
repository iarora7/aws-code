from subapp import app
from flask import Flask, request, jsonify
import psycopg2
import re

# url to use the service
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/fetchFavorite?userId=123456789

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/fetchFavorite", methods=['GET'])
def fetch_user_fav():
    ID = long(request.args.get('userId'))
    cur = conn.cursor()
    cur.execute("SELECT house_id FROM user_fav WHERE user_id = %s", [ID])

    data = cur.fetchall()

    favList = []
    for row in data:

        userFav = {
            'houseId'   :row[0]
        }
        favList.append(userFav)
    
    return jsonify(favList = favList)

@app.route("/fetchHouse", methods=['GET'])
def fetch_user_fav_house():
    ID = int(request.args.get('houseId'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM house_available WHERE id = %s", [ID])

    data = cur.fetchall()

    favHouseList = []
    for row in data:

        userFavHouse = {
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
        favHouseList.append(userFavHouse)

    return jsonify(favHouseList = favHouseList)

@app.route("/addFavHouse", methods=['GET'])
def add_user_fav_house():
    userId = long(request.args.get('userId'))
    houseId = int(request.args.get('houseId'))
    cur = conn.cursor()
    cur.execute("INSERT INTO user_fav VALUES (%s, %s)", (userId,houseId))
    conn.commit()
    return 'true'

@app.route("/removeFavHouse", methods=['GET'])
def remove_user_fav_house():
    userId = long(request.args.get('userId'))
    houseId = int(request.args.get('houseId'))
    cur = conn.cursor()
    cur.execute("DELETE FROM user_fav WHERE user_id=%s AND house_id=%s", (userId,houseId))
    conn.commit()
    return 'true'

@app.route("/checkIfFavHouse", methods=['GET'])
def check_if_user_fav_house():
    userId = long(request.args.get('userId'))
    houseId = int(request.args.get('houseId'))
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM user_fav WHERE user_id=%s AND house_id=%s", (userId,houseId))
    (number_of_rows,)=cur.fetchone()
    if number_of_rows > 0:
        favList = []
        userFav = {
            'value'   :'true'
        }
        favList.append(userFav)

        return jsonify(favList = favList)
    else:
        favList = []
        userFav = {
            'value'   :'false'
        }
        favList.append(userFav)

        return jsonify(favList = favList)
