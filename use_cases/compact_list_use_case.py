from datetime import date, timedelta

from entities.periods_entity import PeriodsEntity


class CompactListUseCase(object):
    list = None

    def __init__(self, list):
        self.list = list

    def run(self):
        compacted_list = []
        previous_period = None
        current_item = None
        for item in self.list:
            if previous_period is not None:
                current_item = item
                if previous_period.end == item.start - timedelta(days=1) and previous_period.has_same_custom_values(item):
                    previous_period.end = item.end
                else:
                    if len(compacted_list) is 0:
                        compacted_list = [previous_period,]
                    else:
                        compacted_list = compacted_list + [previous_period,]
                    previous_period = item
            else:
                previous_period = item
        compacted_list = compacted_list + [current_item, ]
        return compacted_list



