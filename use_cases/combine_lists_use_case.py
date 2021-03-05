class CombineListsUseCase(object):
    list1 = None
    list2 = None
    combined = []

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def run(self):
        current = None
        first_list_size = len(self.list1) -1
        second_list_size = len(self.list2) - 1
        current_first = 0
        current_second = 0

        if self.list1[current_first].start < self.list2[current_second].start:
            current = self.list1[current_first]
            current_first = 1
        else:
            current = self.list2[current_second]
            current_second = 1



        return self.combined
