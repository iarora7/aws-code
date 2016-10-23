from flask import Flask
app = Flask(__name__)

import subapp.addAddress
import subapp.login
import subapp.searchHouseAvailable