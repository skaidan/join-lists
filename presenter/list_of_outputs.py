class ListOfOutputsPresenter(object):
    list = None

    def __init__(self, list):
        self.list = list

    def present(self):
        output = []
        for item in self.list:
            output += [item.__dict__,]

        return output
