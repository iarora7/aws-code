from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

@app.route("/userProfile", methods=['GET', 'POST'])
def save_Address():
    subject = request.args.get('subject')
    addr = request.args.get('addr')
    price = request.args.get('price')
    vacancies = request.args.get('vacancies')
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    description = request.args.get('description')
    phoneNumber = request.args.get('phoneNumber')
    cur = conn.cursor()
    cur.execute("INSERT INTO ADDRESS (SUBJECT, ADDRESS, PRICE, VACANCIES, START_DATE, END_DATE, DESCRIPTION, PHONE_NUMBER) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (subject, addr, price, vacancies, startDate, endDate, description, phoneNumber))
    conn.commit()
    return "Hello"


