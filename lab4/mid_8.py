import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнилась за {end - start:.4f} сек")
        return result
    return wrapper


@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


result = slow_function()
print(f"Результат: {result}")
