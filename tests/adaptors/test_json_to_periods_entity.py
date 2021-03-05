import unittest

from adaptors.json_to_periods_entity import JSONToPeriodsEntityAdaptor
from entities.periods_entity import PeriodsEntity


class JSONToPeriodsEntityTestCase(unittest.TestCase):
    def test_something(self):
        input = self._default_input1()
        adaptor = JSONToPeriodsEntityAdaptor(input)
        periods = adaptor.convert()
        self.assertEqual(len(periods), 8)
        self.assertTrue(isinstance(periods[0], PeriodsEntity))

    @staticmethod
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


if __name__ == '__main__':
    unittest.main()
