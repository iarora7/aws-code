from flask import Flask
app = Flask(__name__)

#import psycopg2
#conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

import subapp.addAddress
import subapp.login
import subapp.searchHouseAvailable