from subapp import app
from flask import request,jsonify
import psycopg2

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

# sample url:
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/getImage?img_id=1
@app.route("/getImage", methods=['GET'])
def getImage():
    img_id = request.args.get('img_id')
    print(img_id)
    cur = conn.cursor()
    cur.execute("Select img_name, encode(img_data,'base64') \
                from images \
                where img_id= %s", (img_id,))
    data = cur.fetchall()
    if(len(data) > 0):
        image = {
        'image_name' : data[0][0],
        'image_data' : data[0][1]
        }    
        
    return jsonify(image = image)      

# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/addImage?img_name=school&img_data=base64string
@app.route("/addImage", methods=['GET']) 
def addImage():
    img_name = request.args.get('img_name')
    img_data = request.args.get('img_data')
    cur = conn.cursor()
    cur.execute("INSERT INTO images (img_name, img_data) \
                VALUES (%s, decode(%s, 'base64'))",
                (img_name, img_data))
    conn.commit()
    return ("image " + img_name + " saved.")