class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        self.amount = int(value - (value * instance.commission))
        return self.amount


class Accaunt:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
