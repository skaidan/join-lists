from entities.periods_entity import PeriodsEntity


class CombineListsUseCase(object):
    list1 = None
    list2 = None
    combined = []

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

        while current_first < first_list_size and current_second < second_list_size:

            # period at second list happens before than period at first
            if self.list1[current_first].start >= self.list2[current_second].end:
                new_period = self.list2[current_first].copy()
                current_second = current_second + 1

            # period at second list starts before than period at first
            elif self.list2[current_second].start <= self.list1[current_first].start:
                new_period = self.list2[current_first].copy()
                new_period.custom_values.update(self.list1[current_first].custom_values)
                # second period is longer than first
                if self.list2[current_second].end >= self.list1[current_first].end:
                    new_period.end = self.list1[current_first].end
                    self.list2[current_second].start = self.list1[current_first].end
                    current_first = current_first + 1
                else:
                    # first period is longer
                    new_period.end = self.list2[current_second].end
                    self.list1[current_first].start = self.list2[current_second].end
                    current_second = current_second + 1

            # period at first list happens before than second
            elif self.list1[current_first].end <= self.list2[current_second].end:
                new_period = self.list1[current_first].copy()
                current_first = current_first + 1

            # period at first list starts before than second
            else:
                new_period = self.list1[current_first].copy()
                new_period.custom_values.update(self.list1[current_first].custom_values)
                # and first is longer
                if self.list1[current_first].end >= self.list2[current_second].end:
                    new_period.end = self.list2[current_second].end
                    self.list1[current_first].start = self.list2[current_second].end
                    current_second = current_second + 1
                else:
                    # and first ends before second
                    self.list1[current_first].start = self.list1[current_first].end

            combined_list = combined_list + [new_period, ]

        return self.combined
