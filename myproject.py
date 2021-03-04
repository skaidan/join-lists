import os
from flask import Flask, jsonify, request
import datetime

from adaptors.json_to_periods_entity import JSONToPeriodsEntityAdaptor
from use_cases.compact_list_use_case import CompactListUseCase

app = Flask(__name__)

#Work with default values
@app.route("/")
def hello():
    input1 = {}
    input2 = {}
    return "<h1 style='color:blue'>Hello Here!</h1>"


@app.route("/custom", methods=['POST', ])
def custom():
    try:
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
    except Exception as e:
        return "Error: No inputs provided."

    period_list1 = JSONToPeriodsEntityAdaptor(input1)
    period_list2 = JSONToPeriodsEntityAdaptor(input2)

    use_case = CompactListUseCase(period_list1)
    period_list1 = use_case.run()

    use_case = CompactListUseCase(period_list2)
    period_list2 = use_case.run()



    now = {'date' : datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") }
    return jsonify(now)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50000))
    app.run(debug=True, host='0.0.0.0', port=port)
