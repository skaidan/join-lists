from datetime import date
import datetime


class PeriodsEntity(object):
    start = None
    end = None
    custom_values = {}

    def __init__(self, period):
        start = period.pop('start', None)
        end = period.pop('end', None)
        custom = period
        try:
            start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
            end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
        except Exception as e:
            print 'It was not possible to parse Period {start} - {end}'.format(start=start, end=end)
        if isinstance(start, date) and isinstance(end, date):
            self.start = start
            self.end = end
            self.custom_values = custom

        else:
            self = None

    def copy(self):
        self_dicted = self.__dict__
        for key, value in self.custom_values.items():
            self_dicted[key] = value
        self_dicted.pop('custom_values')
        new_period = PeriodsEntity(self.__dict__)
        return new_period

    def has_same_custom_values(self, period):
        if len(self.custom_values) is len(period.custom_values):
            for key, val in self.custom_values.iteritems():
                if key not in period.custom_values:
                    return False
            return True
        else:
            return False

    def full_mix(self, period):
        left, right = self._preorder_periods(period)

        first = PeriodsEntity({})
        second = PeriodsEntity({})
        third = PeriodsEntity({})

        first.start = left.start
        if left.end <= right.start:
            self._separated_periods(first, left, right, second)

            # loingituh 2 y first y second are equals

        return [first, second, third]

    @staticmethod
    def _separated_periods(first, left, right, second):
        first.end = left.end
        first.custom_values = left.custom_values
        second.start = right.start
        second.end = right.end
        second.custom_values = right.custom_values

    def _preorder_periods(self, period):
        if self.start <= period.start:
            return self, period
        else:
            return period, self
