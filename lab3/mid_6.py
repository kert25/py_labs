class MathHelper:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привет, я помощник {self.name}!"

    @staticmethod
    def add_numbers(a, b):
        return a + b


helper = MathHelper("Робот-счетчик")
print(helper.greet())

result = MathHelper.add_numbers(15, 27)
print(f"Результат сложения через статический метод: {result}")

print(f"Снова сложили: {helper.add_numbers(10, 5)}")
