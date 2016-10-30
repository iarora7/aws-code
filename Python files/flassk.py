from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")
# print ("Opened database successfully")

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/addr/<addr>", methods=['GET', 'POST'])
def save_Address(addr):
    cur = conn.cursor()
    cur.execute("INSERT INTO HOUSES (ADDRESS) VALUES (%s)", (addr,));
    conn.commit()
    return ('my new address: %s' % addr)

# sample url:
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/login?username=isha&password=13
@app.route("/login", methods=['GET'])
def login_fn():
    name =  request.args.get('username')
    password = request.args.get('password')
    return (name + ":" + password)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)