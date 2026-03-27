squares = {i: i**2 for i in range(1, 11)}
print("Словарь квадратов чисел от 1 до 10:")
for num, square in squares.items():
    print(f"{num} -> {square}")
