from subapp import app
from flask import request, jsonify
import re
import psycopg2

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/getPublicPlaces?option=School
@app.route("/getPublicPlaces", methods=['GET'])
def getPublicPlaces():
	public_place = request.args.get('option')
	cur = conn.cursor()
	cur.execute("Select *, ST_AsText(location)  \
				from public_places p, category c \
				where p.category_id = c.id \
				and c.category_type = %s", (public_place,))
	data = cur.fetchall()

	public_places = []
	for row in data:
		latLongList =  re.findall(r"[-+]?\d*\.\d+|\d+", row[11])
		place = {
			'id'            : row[0],
			'category_id'   : row[1],
			'name'		    : row[2].strip(),
			'st_address'    : row[4],
			'city'          : row[5],
			'state'         : row[6],
			'zip'	 	    : row[7],
			'rating'        : row[8],
			'category_type' : row[10],
			'location'		: row[11],
			'latitude'		: latLongList[1],
			'longitute'		: latLongList[0]
		}
		public_places.append(place)

	return jsonify(public_places = public_places)