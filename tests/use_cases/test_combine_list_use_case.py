import unittest
from flask import jsonify

from myproject import build_list


class CombineListsUseCaseTestCase(unittest.TestCase):

    def test_when_two_lists_are_merged_then_one_list_with_both_custom_fields_grouped_too(self):
        input1 = _default_input1()
        input2 = _default_input2()
        final = build_list(input1, input2)
        self.assertEqual(jsonify(final), _default_output())


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


def _default_output():
    return [
        {
            "start": "2021-02-01",
            "end": "2021-02-05",
            "value": 1,
            "type": "A"
        },
        {
            "start": "2021-02-06",
            "end": "2021-02-06",
            "value": 1,
            "type": "B"
        },
        {
            "start": "2021-02-07",
            "end": "2021-02-09",
            "value": 2,
            "type": "B"
        },
        {
            "start": "2021-02-10",
            "end": "2021-02-10",
            "value": 2,
            "type": "C"
        },
        {
            "start": "2021-02-11",
            "end": "2021-02-11",
            "value": None,
            "type": "C"
        },
        {
            "start": "2021-02-12",
            "end": "2021-02-14",
            "value": 2,
            "type": "C"
        },
        {
            "start": "2021-02-15",
            "end": "2021-02-16",
            "value": 2,
            "type": "A"
        },
        {
            "start": "2021-02-17",
            "end": "2021-02-18",
            "value": 3,
            "type": "A"
        },
        {
            "start": "2021-02-19",
            "end": "2021-02-21",
            "value": 1,
            "type": "A"
        },
        {
            "start": "2021-02-22",
            "end": "2021-02-22",
            "value": 1,
            "type": "C"
        },
        {
            "start": "2021-02-23",
            "end": "2021-02-24",
            "value": 4,
            "type": "C"
        },
        {
            "start": "2021-02-25",
            "end": "2021-02-27",
            "value": 1,
            "type": "B"
        },
        {
            "start": "2021-02-28",
            "end": "2021-02-28",
            "value": 1,
            "type": ""
        },
    ]


if __name__ == '__main__':
    unittest.main()
