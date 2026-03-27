def my_reduce(func, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial
    for item in it:
        value = func(value, item)
    return value


numbers = [1, 2, 3, 4, 5]

total = my_reduce(lambda x, y: x + y, numbers)
product = my_reduce(lambda x, y: x * y, numbers)

print(f"Список: {numbers}")
print(f"Сумма: {total}")
print(f"Произведение: {product}")
