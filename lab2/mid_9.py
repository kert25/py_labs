numbers = [5, 2, 9, 1, 5, 6]


min_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num

print(f"Минимальный элемент: {min_val}")
