import os
from flask import Flask, jsonify
import json
import datetime


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Here!</h1>"

@app.route("/gonzo")
def gonzo():
    return "<h1 style='color:blue'>Hello Gonzo!</h1>"

@app.route("/ahora")
def ahora():
    now = {'date' : datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") }
    return jsonify(now)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50000))
    app.run(debug=True, host='0.0.0.0', port=port)
