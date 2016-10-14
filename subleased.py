from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/")
def hello():
    return "Hello, world!"

# sample url:
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/addAddress?subject=mysub&address=myaddr&price=21&vacancies=2&start_date=2015-3-2&end_date=2015-3-6&description=mydesc&phone_number=324
@app.route("/addAddress", methods=['GET'])
def addAddress():
    subject = request.args.get('subject')
    address = request.args.get('address')
    price   = request.args.get('price')
    vacancies = request.args.get('vacancies')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    description = request.args.get('description')
    phone_number = request.args.get('phone_number')
    cur = conn.cursor()
    cur.execute("INSERT INTO ADDRESS (SUBJECT, ADDRESS, PRICE, \
        VACANCIES, START_DATE, END_DATE, DESCRIPTION, PHONE_NUMBER) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s )", 
    (subject, address, price, vacancies, start_date, end_date, description, phone_number));
    conn.commit()
    return ("address saved with ph: " + phone_number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)