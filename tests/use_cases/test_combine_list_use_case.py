import unittest

from myproject import build_list


class CombineListsUseCaseTestCase(unittest.TestCase):

    def test_when_two_lists_are_merged_then_one_list_with_both_custom_fields_grouped_too(self):
        input1 = _default_input1()
        input2 = _default_input2()
        final = build_list(input1, input2)
        self.asset_morfology_matches(final)

    def asset_morfology_matches(self, final):
        self.assertEqual(len(final), 13)
        self.assertEqual(len(final[0].custom_values), 2)
        self.assertEqual(len(final[1].custom_values), 2)
        self.assertEqual(len(final[2].custom_values), 2)
        self.assertEqual(len(final[3].custom_values), 2)
        self.assertEqual(len(final[4].custom_values), 1)
        self.assertEqual(len(final[5].custom_values), 2)
        self.assertEqual(len(final[6].custom_values), 2)
        self.assertEqual(len(final[7].custom_values), 2)
        self.assertEqual(len(final[8].custom_values), 2)
        self.assertEqual(len(final[9].custom_values), 2)
        self.assertEqual(len(final[10].custom_values), 2)
        self.assertEqual(len(final[11].custom_values), 2)
        self.assertEqual(len(final[12].custom_values), 1)


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


if __name__ == '__main__':
    unittest.main()
