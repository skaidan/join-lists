from entities.periods_entity import PeriodsEntity


class JSONToPeriodsEntityAdaptor(object):
    data = None

    def __init__(self, input):
        self.data = input

    def convert(self):
        periods = []
        for item in self.data:
            periods = periods + [PeriodsEntity(item),]
        return periods