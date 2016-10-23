from subapp import app
from flask import Flask, request

# sample url:
# http://ec2-52-53-202-11.us-west-1.compute.amazonaws.com:8080/login?username=isha&password=13
@app.route("/login", methods=['GET'])
def login_fn():
    name =  request.args.get('username')
    password = request.args.get('password')
    return (name + ":" + password)
