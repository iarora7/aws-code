from flask import Flask, request
import psycopg2

# Demo flask service api

app = Flask(__name__)

conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")


@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/next")
def next_route():
    return "This is next page"

@app.route("/addr/<addr>", methods=['GET', 'POST'])
def save_Address(addr):
    cur = conn.cursor()
    cur.execute("INSERT INTO HOUSES (ADDRESS) VALUES (%s)", addr);
    return ('my new address: %s' % addr)

@app.route("/login", methods=['GET'])
def login_fn():
    return request.args.get[username]



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)