import unittest
import datetime

from entities.periods_entity import PeriodsEntity
from use_cases.compact_list_use_case import CompactListUseCase


class CompactListUseCaseTestCase(unittest.TestCase):

    def test_when_list_does_not_contain_continuous_periods_then_list_is_not_modified(self):
        periods = [PeriodsEntity({'start': "2021-02-23", 'end': "2021-02-23", 'first': 1}), PeriodsEntity(
            {'start': "2021-02-25", 'end': "2021-02-25", 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 2)
        self.assertEqual(compacted_list[0].end, datetime.date(2021, 2, 23))
        self.assertEqual(compacted_list[1].start, datetime.date(2021, 2, 25))

    def test_when_list_contain_two_continuous_periods_then_they_are_compacted_into_one(self):
        periods = [PeriodsEntity({'start': "2021-02-23", 'end': "2021-02-23", 'first': 1}), PeriodsEntity(
            {'start': "2021-02-24", 'end': "2021-02-25", 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 1)
        self.assertEqual(compacted_list[0].end, datetime.date(2021, 2, 25))

    def test_when_list_contain_two_pairs_of_continuous_periods_then_they_are_compacted_independiently(self):
        periods = [PeriodsEntity({'start': "2021-02-23", 'end': "2021-02-23", 'first': 1}), PeriodsEntity(
            {'start': "2021-02-24", 'end': "2021-02-25", 'first': 1}),
                   PeriodsEntity({'start': "2021-02-27", 'end': "2021-03-01",
                                  'first': 1}),
                   PeriodsEntity({'start': "2021-03-03", 'end': "2021-03-05",
                                  'first': 1}), PeriodsEntity(
                {'start': "2021-03-06", 'end': "2021-03-06", 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 3)


if __name__ == '__main__':
    unittest.main()
