import os
from flask import Flask, jsonify, request

from adaptors.json_to_periods_entity import JSONToPeriodsEntityAdaptor
from presenter.list_of_outputs import ListOfOutputsPresenter
from use_cases.combine_lists_use_case import CombineListsUseCase
from use_cases.compact_list_use_case import CompactListUseCase

app = Flask(__name__)


# Work with default values
def _default_input1():
    return [
        {
            "start": "2021-02-01",
            "end": "2021-02-04",
            "value": 1
        },
        {
            "start": "2021-02-05",
            "end": "2021-02-06",
            "value": 1
        },
        {
            "start": "2021-02-07",
            "end": "2021-02-10",
            "value": 2
        },
        {
            "start": "2021-02-12",
            "end": "2021-02-16",
            "value": 2
        },
        {
            "start": "2021-02-17",
            "end": "2021-02-18",
            "value": 3
        },
        {
            "start": "2021-02-19",
            "end": "2021-02-22",
            "value": 1
        },
        {
            "start": "2021-02-23",
            "end": "2021-02-24",
            "value": 4
        },
        {
            "start": "2021-02-25",
            "end": "2021-02-28",
            "value": 1
        },
    ]


def _default_input2():
    return [
        {
            "start": "2021-02-01",
            "end": "2021-02-05",
            "type": "A"
        },
        {
            "start": "2021-02-06",
            "end": "2021-02-09",
            "type": "B"
        },
        {
            "start": "2021-02-10",
            "end": "2021-02-14",
            "type": "C"
        },
        {
            "start": "2021-02-15",
            "end": "2021-02-18",
            "type": "A"
        },
        {
            "start": "2021-02-19",
            "end": "2021-02-21",
            "type": "A"
        },
        {
            "start": "2021-02-22",
            "end": "2021-02-24",
            "type": "C"
        },
        {
            "start": "2021-02-25",
            "end": "2021-02-27",
            "type": "B"
        },
    ]


@app.route("/")
def default():
    input1 = _default_input1()
    input2 = _default_input2()
    final = build_list(input1, input2)
    presenter = ListOfOutputsPresenter(final)
    return str(presenter.present())


def build_list(input1, input2):
    period_list1 = JSONToPeriodsEntityAdaptor(input1)
    period_list2 = JSONToPeriodsEntityAdaptor(input2)
    use_case = CompactListUseCase(period_list1.convert())
    period_list1 = use_case.run()
    use_case = CompactListUseCase(period_list2.convert())
    period_list2 = use_case.run()
    use_case = CombineListsUseCase(period_list1, period_list2)
    combined = use_case.run()
    use_case = CompactListUseCase(combined)
    final = use_case.run()
    return final


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50000))
    app.run(debug=True, host='0.0.0.0', port=port)
