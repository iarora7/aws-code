from subapp import app
from flask import Flask, request
import psycopg2

# url to use the service
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/fbLogin?id=36&full_name=fullname&first_name=fname&last_name=lname

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/fbLogin", methods=['GET'])
def fb_login():
    user_id = long(request.args.get('id'))
    full_name = None #request.args.get('full_name')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = None
    email = None

    cur = conn.cursor()
    cur.execute("SELECT id FROM user_profile WHERE id = %s", [user_id])

    data = cur.fetchall()

    if str(user_id) in str(data):
        result = 'true'
    else:
        result = 'false'
        cur.execute("INSERT INTO USER_PROFILE (ID, FULL_NAME, FIRST_NAME, \
             LAST_NAME, PHONE_NUMBER, EMAIL) \
        VALUES (%s, %s, %s, %s, %s, %s)",
        (user_id, full_name, first_name, last_name, phone_number, email));
        conn.commit()


    return result
