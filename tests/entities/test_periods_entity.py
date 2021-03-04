import unittest
from datetime import date, timedelta
from entities.periods_entity import PeriodsEntity


class PeriodsEntityTestCase(unittest.TestCase):

    def test_when_there_is_no_start_date_then_period_is_none(self):
        period_without_start_date = {'end': date.today()}
        period = PeriodsEntity(period_without_start_date)
        self.assertEqual(period.start, None)

    def test_when_there_is_no_end_date_then_period_is_none(self):
        period_without_end_date = {'start': date.today()}
        period = PeriodsEntity(period_without_end_date)
        self.assertEqual(period.end, None, "It was expected empty object")

    def test_when_there_is_a_extra_custom_fields_then_they_are_added_to_the_entity(self):
        expected_value = 1
        period_extra = {'start': date.today(), 'end': date.today(), 'single': expected_value}
        period = PeriodsEntity(period_extra)
        self.assertEqual(len(period.custom_values), 1, 'Expected value mismatch')
        self.assertEqual(period.custom_values['single'], expected_value, 'Expected value mismatch')

    def test_when_there_are_extra_custom_fields_then_they_are_added_to_the_entity(self):
        expected_numeric_value = 1
        expected_text_value = 't'
        period_extra = {'start': date.today(), 'end': date.today(), 'first': expected_numeric_value,
                        'second': expected_text_value}
        period = PeriodsEntity(period_extra)
        self.assertEqual(len(period.custom_values), 2)
        self.assertEqual(period.custom_values['second'], expected_text_value, 'Expected value mismatch')
        self.assertEqual(period.custom_values['first'], expected_numeric_value, 'Expected value mismatch')

    def test_when_a_period_entity_is_copied_then_a_new_object_is_created(self):
        period = {'start': date.today(), 'end': date.today(), 'first': 1,
                        'second': 2}
        period = PeriodsEntity(period)
        new_period = period.copy()
        period.custom_values['first'] = 3
        self.assertEqual(new_period.custom_values['first'], 1, "Error, first value should not be modified")
        self.assertEqual(period.custom_values['first'], 3, "Error, first value should be updated")

    def test_when_there_are_two_period_equals_then_mix_is_just_one_period_with_all_custom_fields(self):
        first_period = PeriodsEntity({'start': date.today(), 'end': date.today(), 'first': 1})
        second_period = PeriodsEntity({'start': date.today(), 'end': date.today(), 'second': 'a'})
        period_join = first_period.full_mix(second_period)
        self.assertEqual(len(period_join), 1, "Error, 1 period should be returned")
        self.assertEqual(len(period_join[0].custom_values), 2, "Error, 2 different custom fields should be returned")

    def test_when_there_are_two_period_and_one_contains_other_then_mix_is_the_contained_plus_one_on_each_extreme(self):
        yesterday = date.today() - timedelta(days=1)
        tomorrow = date.today() + timedelta(days=1)
        period_bigger = PeriodsEntity({'start': yesterday, 'end': tomorrow})
        period_smaller = PeriodsEntity({'start': date.today(), 'end': date.today()})
        period_join = period_bigger.full_mix(period_smaller)
        self.assertEqual(len(period_join), 3, "Error, 3 different periods should be returned")
        self.assertEqual(period_join.start, period_smaller['start'], "Error, 3 different periods should be returned")
        self.assertEqual(period_join.end, period_smaller['end'], "Error, 3 different periods should be returned")


if __name__ == '__main__':
    unittest.main()
