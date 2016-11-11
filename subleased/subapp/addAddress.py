from subapp import app
from flask import request
import psycopg2

conn = psycopg2.connect(database="geodb", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/")
def hi():
    return "Hi there, world!"

# sample url:
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/addAddress?title=mytitle&address=myaddr&aptNum=2&city=mycity&state=mystate&zipcd=90007&price=21&vacancies=2&start_date=2015-3-2&end_date=2015-3-6&description=mydesc&phone_number=324&lat=34.031096&lng=-118.289951
@app.route("/addAddress", methods=['GET'])
def addAddress():
    title = request.args.get('title')
    address = request.args.get('address')
    aptNum = request.args.get('aptNum')
    if aptNum is None:
        aptNum = 0
    city = request.args.get('city')
    state = request.args.get('state')
    zipcd = request.args.get('zipcd')
    price   = request.args.get('price')
    vacancies = request.args.get('vacancies')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    description = request.args.get('description')
    phone_number = request.args.get('phone_number')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    available = "true"
    location = "POINT(%s %s)" % (lng, lat)
    cur = conn.cursor()
    cur.execute("INSERT INTO house_available (user_id, st_address, apt_no, city, state, zip, spots, price, \
        start_date, end_date, title, description, phone_number, available, location) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326))",
    (1349781218406667, address, aptNum, city, state, zipcd, vacancies, price, start_date, end_date, \
        title, description, phone_number, available, location));
    conn.commit()
    return ("address saved with ph: " + phone_number)