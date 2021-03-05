import unittest
from entities.periods_entity import PeriodsEntity


class PeriodsEntityTestCase(unittest.TestCase):

    def test_when_there_is_no_start_date_then_period_is_none(self):
        period_without_start_date = {'end': "2021-02-23"}
        period = PeriodsEntity(period_without_start_date)
        self.assertEqual(period.start, None)

    def test_when_there_is_no_end_date_then_period_is_none(self):
        period_without_end_date = {'start': "2021-02-23"}
        period = PeriodsEntity(period_without_end_date)
        self.assertEqual(period.end, None, "It was expected empty object")

    def test_when_there_is_a_extra_custom_fields_then_they_are_added_to_the_entity(self):
        expected_value = 1
        period_extra = {'start': "2021-02-23", 'end': "2021-02-23", 'single': expected_value}
        period = PeriodsEntity(period_extra)
        self.assertEqual(len(period.custom_values), 1, 'Expected value mismatch')
        self.assertEqual(period.custom_values['single'], expected_value, 'Expected value mismatch')

    def test_when_there_are_extra_custom_fields_then_they_are_added_to_the_entity(self):
        expected_numeric_value = 1
        expected_text_value = 't'
        period_extra = {'start': "2021-02-23", 'end': "2021-02-23", 'first': expected_numeric_value,
                        'second': expected_text_value}
        period = PeriodsEntity(period_extra)
        self.assertEqual(len(period.custom_values), 2)
        self.assertEqual(period.custom_values['second'], expected_text_value, 'Expected value mismatch')
        self.assertEqual(period.custom_values['first'], expected_numeric_value, 'Expected value mismatch')

    def test_when_a_period_entity_is_copied_then_a_new_object_is_created(self):
        period = {'start': "2021-02-23", 'end': "2021-02-23", 'first': 1,
                  'second': 2}
        period = PeriodsEntity(period)
        new_period = period.copy()
        period.custom_values['first'] = 3
        self.assertEqual(new_period.custom_values['first'], 1, "Error, first value should not be modified")
        self.assertEqual(period.custom_values['first'], 3, "Error, first value should be updated")


if __name__ == '__main__':
    unittest.main()
