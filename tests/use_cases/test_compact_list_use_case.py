import unittest
from datetime import date, timedelta

from entities.periods_entity import PeriodsEntity
from use_cases.compact_list_use_case import CompactListUseCase


class CompactListUseCaseTestCase(unittest.TestCase):

    def test_when_list_does_not_contain_continuous_periods_then_list_is_not_modified(self):
        periods = [PeriodsEntity({'start': date.today(), 'end': date.today(), 'first': 1}), PeriodsEntity(
            {'start': date.today() + timedelta(days=1), 'end': date.today() + timedelta(days=2), 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 1)
        self.assertEqual(compacted_list[0].end, date.today() + timedelta(days=2))

    def test_when_list_contain_two_continuous_periods_then_they_are_compacted_into_one(self):
        periods = [PeriodsEntity({'start': date.today(), 'end': date.today(), 'first': 1}), PeriodsEntity(
            {'start': date.today() + timedelta(days=1), 'end': date.today() + timedelta(days=2), 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 1)
        self.assertEqual(compacted_list[0].end, date.today() + timedelta(days=2))

    def test_when_list_contain_two_pairs_of_continuous_periods_then_they_are_compacted_independiently(self):
        periods = [PeriodsEntity({'start': date.today(), 'end': date.today(), 'first': 1}), PeriodsEntity(
            {'start': date.today() + timedelta(days=1), 'end': date.today() + timedelta(days=2), 'first': 1}),
                   PeriodsEntity({'start': date.today() + timedelta(days=4), 'end': date.today() + timedelta(days=6),
                                  'first': 1}),
                   PeriodsEntity({'start': date.today() + timedelta(days=8), 'end': date.today() + timedelta(days=10),
                                  'first': 1}), PeriodsEntity(
                {'start': date.today() + timedelta(days=11), 'end': date.today() + timedelta(days=12), 'first': 1})]
        use_case = CompactListUseCase(periods)
        compacted_list = use_case.run()
        self.assertEqual(len(compacted_list), 3)


if __name__ == '__main__':
    unittest.main()
