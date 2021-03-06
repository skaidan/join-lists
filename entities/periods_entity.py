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
            print 'It was not possible to parse Period ( {start} - {end} )'.format(start=start, end=end)
        if isinstance(start, date) and isinstance(end, date):
            self.start = start
            self.end = end
            self.custom_values = custom

        else:
            self = None

    def copy(self):
        new_period = PeriodsEntity({})
        new_period.start = self.start
        new_period.end = self.end
        if self.custom_values:
            new_period.custom_values = dict(self.custom_values)
        return new_period

    def has_same_custom_values(self, period):
        if len(self.custom_values) is len(period.custom_values):
            for key, val in self.custom_values.iteritems():
                if key not in period.custom_values:
                    return False
                if val != period.custom_values[key]:
                    return False
            return True
        else:
            return False

    @staticmethod
    def _redux_list(periods):
        reduxed = []
        for i in periods:
            if i.start:
                reduxed = reduxed + [i,]
        return reduxed

    def _preorder_periods(self, period):
        if self.start <= period.start:
            return self, period
        else:
            return period, self
