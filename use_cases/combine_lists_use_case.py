from entities.periods_entity import PeriodsEntity
from datetime import timedelta


class CombineListsUseCase(object):
    list1 = None
    list2 = None

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def run(self):
        new_period = None
        combined_list = []
        first_list_size = len(self.list1) - 1
        second_list_size = len(self.list2) - 1
        current_first = 0
        current_second = 0

        while current_first <= first_list_size and current_second <= second_list_size:

            # first period happens before than second
            if self.list2[current_second].start > self.list1[current_first].end:
                new_period = self.list1[current_first].copy()
                current_first = current_first + 1

            # period at second list happens before than period at first
            elif self.list1[current_first].start > self.list2[current_second].end:
                new_period = self.list2[current_second].copy()
                current_second = current_second + 1

            #######################################################################################

            # period at second list starts before than period at first
            elif self.list2[current_second].start < self.list1[current_first].start:
                new_period = self.list2[current_second].copy()
                new_period.end = self.list1[current_first].start - timedelta(days=1)
                self.list2[current_second].start = self.list1[current_first].start

            # period at first list starts before than period at second
            elif self.list1[current_first].start < self.list2[current_second].start:
                new_period = self.list1[current_first].copy()
                new_period.end = self.list2[current_second].start - timedelta(days=1)
                self.list1[current_first].start = self.list2[current_second].start


            ############################both start at same day######################################

            # period at first list finishes before than second
            elif self.list1[current_first].end < self.list2[current_second].end:
                new_period = self.list1[current_first].copy()
                new_period.custom_values.update(self.list2[current_second].custom_values)
                self.list2[current_second].start = self.list1[current_first].end + timedelta(days=1)
                current_first = current_first + 1

            # period at second list finishes before than first
            elif self.list2[current_second].end < self.list1[current_first].end:
                new_period = self.list2[current_second].copy()
                new_period.custom_values.update(self.list1[current_first].custom_values)
                self.list1[current_first].start = self.list2[current_second].end + timedelta(days=1)
                current_second = current_second + 1

            # both end at same place
            else:
                new_period = self.list2[current_second].copy()
                new_period.custom_values.update(self.list1[current_first].custom_values)
                current_second = current_second + 1
                current_first = current_first + 1

            combined_list = combined_list + [new_period, ]

        while current_first <= first_list_size:
            combined_list = combined_list + [self.list1[current_first], ]
            current_first = current_first + 1

        while current_second <= second_list_size:
            combined_list = combined_list + [self.list2[current_second], ]
            current_second = current_second + 1

        return combined_list
