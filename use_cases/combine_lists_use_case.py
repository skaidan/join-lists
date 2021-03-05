class CombineListsUseCase(object):
    list1 = None
    list2 = None
    combined = []

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def run(self):
        return self.combined
