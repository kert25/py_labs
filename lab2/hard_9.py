def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)


number = 5
result = recursive_sum(number)
print(f"Сумма чисел от 1 до {number} равна {result}")
