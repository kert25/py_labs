class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value


counter = Counter()
print(f"Начальное значение: {counter.get_value()}")

counter.increment()
counter.increment()
counter.increment()
print(f"После 3 увеличений: {counter.get_value()}")

counter.decrement()
print(f"После 1 уменьшения: {counter.get_value()}")
