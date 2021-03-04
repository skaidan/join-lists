import os
from flask import Flask, jsonify
import datetime


app = Flask(__name__)

#Work with default values
@app.route("/")
def hello():
    input1 = {}
    input2 = {}
    return "<h1 style='color:blue'>Hello Here!</h1>"


@app.route("/custom", methods=['POST', ])
def custom():
    input1 = {}
    input2 = {}
    now = {'date' : datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") }
    return jsonify(now)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50000))
    app.run(debug=True, host='0.0.0.0', port=port)
